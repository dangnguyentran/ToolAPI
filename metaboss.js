const WebSocket = require('ws');
const fs = require('fs');

const wsUrl = 'wss://apiv2.metaboss.xyz:2000/game';
const ws = new WebSocket(wsUrl);

let isBossDead = false;
let isDelayActive = false;
let clickInterval;
let totalCoin = 0;
let countdownInterval;
let hashDataArray = [];
let currentHashIndex = 0;

const colors = {
  'reset': '\x1b[0m',
  'green': '\x1b[32m',
  'yellow': '\x1b[33m',
  'red': '\x1b[31m',
  'blue': '\x1b[34m',
  'magenta': '\x1b[35m',
  'cyan': '\x1b[36m',
  'white': '\x1b[37m'
};

function getRandomColor() {
  const colorKeys = Object.keys(colors);
  const randomIndex = Math.floor(Math.random() * (colorKeys.length - 1)) + 1;
  return colors[colorKeys[randomIndex]];
}

function readHashFromFile(filePath) {
  try {
    const data = fs.readFileSync(filePath, 'utf8');
    return data.split('\n').map(line => JSON.parse(line));
  } catch (error) {
    console.error(getRandomColor() + 'Không thể đọc dữ liệu từ tệp:', error.message + colors.reset);
    return null;
  }
}

function formatDate(date) {
  return '[' + date.getHours().toString().padStart(2, '0') + ':' +
    date.getMinutes().toString().padStart(2, '0') + ', ' +
    date.getDate().toString().padStart(2, '0') + '/' +
    (date.getMonth() + 1).toString().padStart(2, '0') + '/' +
    date.getFullYear() + ' ]';
}

function processNextHash() {
  if (currentHashIndex < hashDataArray.length) {
    ws.send(JSON.stringify(hashDataArray[currentHashIndex]));
    currentHashIndex++;
    setTimeout(processNextHash, 2000);
  } else {
    startCountdown();
  }
}

function startCountdown() {
  console.log(`${getRandomColor()}[ - ] Đã hoàn thành tất cả các hash. Trì hoãn 40 phút trước khi bắt đầu lại.${colors.reset}`);
  let remainingTime = 90 * 60; // 90 minutes in seconds
  countdownInterval = setInterval(() => {
    const minutes = Math.floor(remainingTime / 60);
    const seconds = remainingTime % 60;
    process.stdout.write(`\r${getRandomColor()}==========Thời gian còn lại: ${minutes}:${seconds.toString().padStart(2, '0')}==========${colors.reset}`);
    remainingTime--;

    if (remainingTime < 0) {
      clearInterval(countdownInterval);
      currentHashIndex = 0;
      processNextHash();
    }
  }, 1000);
}

function handleOpen() {
  hashDataArray = readHashFromFile('hashmetaboss.txt');
  if (hashDataArray) {
    processNextHash();
  } else {
    console.error(getRandomColor() + '[ - ] Không đọc được dữ liệu xác thực từ hash.txt' + colors.reset);
  }
}

function handleIncoming(data) {
  const message = data.toString();
  const parsedData = JSON.parse(message);
  let logMessage = '';

  const date = new Date();
  const formattedDate = formatDate(date);

  if (parsedData.code === 2) {
    const { id, name, coin } = parsedData.data;
    totalCoin = coin;
    logMessage = `${formattedDate} ${getRandomColor()}\n[ + ] ID Telegram : ${id}\n[ + ] Tài khoản : ${name}\n[ + ] Coin hiện tại : ${coin}${colors.reset}`;
    clickInterval = setInterval(() => {
      ws.send('{"code":1,"type":3,"data":{}}');
    }, 1000);
  }

  if (parsedData.code === 10) {
    const { coin, hpBoss } = parsedData.data;
    totalCoin = coin;
    logMessage = `${formattedDate} ${getRandomColor()}\n[ +1 ], Tất cả Coin ${totalCoin}, Máu Boss ${hpBoss}\n${colors.reset}`;

    if (parsedData.data.hpBoss === 0 && !isDelayActive) {
      isDelayActive = true;
      console.log(`${formattedDate} ${getRandomColor()}\n[ - ] BOSS CHẾT. Trì hoãn 40 phút trước khi tiếp tục nhấp chuột.${colors.reset}`);
      clearInterval(clickInterval);

      let remainingTime = 40 * 60; // 40 minutes in seconds
      countdownInterval = setInterval(() => {
        const minutes = Math.floor(remainingTime / 60);
        const seconds = remainingTime % 60;
        process.stdout.write(`\r${getRandomColor()}==========Thời gian còn lại: ${minutes}:${seconds.toString().padStart(2, '0')}==========\n${colors.reset}`);
        remainingTime--;

        if (remainingTime < 0) {
          clearInterval(countdownInterval);
          isDelayActive = false;
          console.log(`\n${formattedDate} ${getRandomColor()}\n[ - ] 90 phút đã trôi qua. Tiếp tục bấm.${colors.reset}`);
          clickInterval = setInterval(() => {
            ws.send('{"code":1,"type":3,"data":{}}');
          }, 1000);
        }
      }, 1000);
    }
  }

  if (logMessage) {
    console.log(logMessage);
  }
}

function handleClose() {
  const date = new Date();
  const formattedDate = formatDate(date);
  console.log(`${formattedDate} ${getRandomColor()}[ - ] Kêt nôi bị mất.${colors.reset}`);
}

function handleError(error) {
  const date = new Date();
  const formattedDate = formatDate(date);
  console.error(`${formattedDate} ${getRandomColor()}[ - ] Có lỗi: ${error.message}${colors.reset}`);
}

ws.on('open', handleOpen);
ws.on('message', handleIncoming);
ws.on('close', handleClose);
ws.on('error', handleError);
