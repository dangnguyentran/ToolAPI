const axios = require('axios');
const fs = require('fs');
const readline = require('readline');


let queries = [];
try {
  const data = fs.readFileSync('queryspinnercoin.txt', 'utf8');
  queries = data.split('\n').map(line => line.trim().replace(/\r$/, '')).filter(line => line !== '');
} catch (err) {
  console.error('Không thể đọc file queryspinnercoin.txt:', err);
  process.exit(1);
}

let currentQueryIndex = 0;
let currentProxyIndex = 0;
let upgradeSpinner = false;

function getCurrentQueryId() {
  return queries[currentQueryIndex];
}

function nextQueryId() {
    currentQueryIndex += 1;
     if (currentQueryIndex >= queries.length) {
        currentQueryIndex = 0;
        console.log('Đã spin hết tất cả tài khoản.');
        return false;
    } else {
        const initData = getCurrentQueryId();
        const decoded = decodeURIComponent(initData);
        const userPattern = /user=([^&]+)/;
        const userMatch = decoded.match(userPattern);
        if (userMatch && userMatch[1]) {
            const userInfoStr = userMatch[1];
            try {
                const userInfo = JSON.parse(userInfoStr);
                console.log(`[*] Chuyển sang tài khoản ${userInfo.first_name} ${userInfo.last_name}`);
            } catch (error) {
                console.error('Lỗi phân tích thông tin người dùng:', error);
            }
        } else {
            console.log('Không thể tìm thông tin người dùng trong initData');
        }
    }
    return true;
}

function getClick() {
    return Math.floor(Math.random() * 11) + 20;
}

let payloadspin = {
    "initData": getCurrentQueryId(),
    "data": { "clicks": getClick(), "isClose": null }
};

async function callSpinAPI() {
    payloadspin.initData = getCurrentQueryId();
    try {
        const response = await axios.post('https://back.timboo.pro/api/upd-data', payloadspin, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
    } catch (error) {
        handleAPIError(error, 'first API');
        if (error.response && error.response.data.message === 'Data acquisition error1') {
            console.log('Lỗi thu thập dữ liệu, chuyển tài khoản tiếp theo...');
        }
    }
}

async function callRepairAPI() {
  const payloadRepairAPI = {
    "initData": getCurrentQueryId()
  };

  try {
    await axios.post('https://back.timboo.pro/api/repair-spinner', payloadRepairAPI, {
      headers: {
        'Content-Type': 'application/json'
      }
      
    });

    console.log('Sửa spin thành công.');
  } catch (error) {
    handleAPIError(error, 'repair API');
  }
}

async function spinAllSpinners() {
    const payloadlayData = {
        "initData": getCurrentQueryId()
    };

    try {
        const response = await axios.post('https://back.timboo.pro/api/init-data', payloadlayData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });

    let responseData = response.data;
    let spinners = responseData.initData.spinners;

    while (spinners.some(spinner => !spinner.isBroken)) {
      const spinPromises = spinners.filter(spinner => !spinner.isBroken).map(spinner => callSpinAPI());
      await Promise.all(spinPromises);

      response = await axios.post('https://back.timboo.pro/api/init-data', payloadlayData, {
        headers: {
          'Content-Type': 'application/json'
        }
        
      });

      responseData = response.data;
      spinners = responseData.initData.spinners;

      const { balance, league } = responseData.initData.user;
      const spinnerHPs = spinners.map(s => s.hp);
      console.log(`Spin thành công: Balance: ${balance}, League: ${league.name}, Spinner HP: ${spinnerHPs.join(', ')}`);
    }

    const brokenSpinners = spinners.filter(spinner => spinner.isBroken && spinner.endRepairTime === null);
    if (brokenSpinners.length > 0) {
      await callRepairAPI();
    }
  } catch (error) {
    handleAPIError(error, 'spinAllSpinners function');
  }
}

function countdown(duration) {
  let remaining = duration;

  const countdownInterval = setInterval(() => {
    const hours = Math.floor(remaining / 3600);
    const minutes = Math.floor((remaining % 3600) / 60);
    const seconds = remaining % 60;

    const timeString = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    process.stdout.write(`\rThời gian còn lại: ${timeString}`);

    remaining -= 1;

    if (remaining < 0) {
      clearInterval(countdownInterval);
      process.stdout.write('\rHoàn tất!                \n');
    }
  }, 1000);
}

async function layData() {
  await checkAndOpenBox();
  const spinnerId = await getSpinnerId();
  if (upgradeSpinner && spinnerId) {
    await callUpgradeAPI(spinnerId);
  }
  await spinAllSpinners();
  const hasNextQuery = nextQueryId();
  if (!hasNextQuery) {
    const endRepairTime = await getEndRepairTime();
    if (endRepairTime) {
      const now = new Date();
      const nowUTC = new Date(now.toISOString()); 
      const waitTime = endRepairTime.getTime() - nowUTC.getTime();  
      if (waitTime > 0) {
        console.log(`Chờ đến thời gian: ${endRepairTime.toISOString()}`);
        countdown(waitTime / 1000);
        await new Promise(resolve => setTimeout(resolve, waitTime));
      }
    }
    return;
  }
  
}
async function callUpgradeAPI(spinnerId) {
  const payloadUpgradeAPI = {
    "initData": getCurrentQueryId(),
    "spinnerId": spinnerId
  };

  while (true) {
    try {
      await axios.post('https://back.timboo.pro/api/upgrade-spinner', payloadUpgradeAPI, {
        headers: {
          'Content-Type': 'application/json'
        }
        
      });

      console.log('Nâng cấp spinner thành công.');
    } catch (error) {
      if (error.response && error.response.data.message === "Error, the spinner hasn't upgraded.") {
        console.log('Không thể nâng spin.');
        break;
      } else {
        handleAPIError(error, 'upgrade-spinner API');
      }
    }
  }
}
async function getSpinnerId() {
  const payload = {
    "initData": getCurrentQueryId()
  };

  try {
    const response = await axios.post('https://back.timboo.pro/api/init-data', payload, {
      headers: {
        'Content-Type': 'application/json'
      }
     
    });

    if (response.status === 200 && response.data && response.data.initData && response.data.initData.spinners) {
      const spinners = response.data.initData.spinners;
      if (spinners.length > 0) {
        return spinners[0].id; 
      }
    } else {
      console.log('Không nhận được spinner ID từ API.');
    }
  } catch (error) {
    handleAPIError(error, 'getSpinnerId API');
  }
  return null;
}
async function askForUpgrade() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  return new Promise(resolve => {
    rl.question('Bạn có muốn nâng cấp spinner này không? (y/n): ', (answer) => {
      if (answer.toLowerCase() === 'y' || answer.toLowerCase() === 'n') {
        upgradeSpinner = answer.toLowerCase() === 'y';
        rl.close();
        resolve();
      } else {
        console.error('Trả lời không hợp lệ. Vui lòng nhập "y" hoặc "n".');
        rl.close();
        process.exit(1);
      }
    });
  });
}
async function getEndRepairTime() {
  const payload = {
    "initData": getCurrentQueryId()
  };

  try {
    const response = await axios.post('https://back.timboo.pro/api/init-data', payload, {
      headers: {
        'Content-Type': 'application/json'
      }
      
    });

    if (response.status === 200 && response.data) {
      if (!response.data.initData.spinners || response.data.initData.spinners.length === 0 || !response.data.initData.spinners[0].endRepairTime) {
        console.log('Không có thông tin endRepairTime từ API.');
        return null;
      }

      const endRepairTime = new Date(response.data.initData.spinners[0].endRepairTime);
      endRepairTime.setHours(endRepairTime.getHours()); 
      endRepairTime.setMinutes(endRepairTime.getMinutes() + 30); 
      return endRepairTime;
    } else {
      console.log('Không nhận được endRepairTime từ API.', response.data);
    }
  } catch (error) {
    handleAPIError(error, 'getEndRepairTime API');
  }

  return null;
}

function shouldOpenBox(box) {
  const nowUTC = Date.now();

  const openTimeUTC = box.open_time ? new Date(box.open_time).getTime() : null;

  if (!openTimeUTC) {
    console.log('Không có thời gian mở hộp, mở hộp ngay.');
    return true;
  }

  const fiveHoursInMillis = 5 * 60 * 60 * 1000;
  const fiveHoursAfterOpenTimeUTC = openTimeUTC + fiveHoursInMillis;

  return nowUTC > fiveHoursAfterOpenTimeUTC;
}

async function checkAndOpenBox() {
    console.log('Đang kiểm tra và mở hộp...');
    const payload = {
        "initData": getCurrentQueryId()
    };

    try {
        const response = await axios.post('https://api.timboo.pro/get_data', payload, {
            headers: {
                'Content-Type': 'application/json'
            }
        });

    if (response.status === 200 && response.data && response.data.boxes) {
      const boxes = response.data.boxes;

      const boxToOpen = boxes.find(box => shouldOpenBox(box));

            if (boxToOpen) {
                console.log(`Mở hộp ${boxToOpen.name}...`);
                const openBoxPayload = {
                    "initData": getCurrentQueryId(),
                    "boxId": boxToOpen.id
                };

        try {
          const openBoxResponse = await axios.post('https://api.timboo.pro/open_box', openBoxPayload, {
            headers: {
              'Content-Type': 'application/json'
            }
            
          });
          if (openBoxResponse.status === 200) {
            console.log(`Đã mở hộp ${boxToOpen.name}.`);
          } else {
            console.log('Mở hộp thất bại với mã trạng thái:', openBoxResponse.status);
          }
        } catch (error) {
          console.error('Chưa đến thời gian mở hộp');
        }
      } else {
        console.log('Không có hộp nào để mở.');
      }
    } else {
      console.log('Không nhận được dữ liệu hộp hợp lệ từ API.');
    }
    } catch (error) {
        handleAPIError(error, 'checkAndOpenBox API');
  }

    }


function handleAPIError(error, apiName) {
    if (error.response) {
        console.error(`Lỗi ${apiName}:`, error.response.data);
        console.error('Trạng thái:', error.response.status);
    } else if (error.request) {
        console.error(`Không nhận được phản hồi từ ${apiName}:`, error.request);
    } else {
        console.error(`Lỗi rồi ${apiName}:`, error.message);
    }
}

async function startLoop() {
await askForUpgrade(); 
    while (true) {
        
        await layData();
        await new Promise(resolve => setTimeout(resolve, 0));
    }
}

startLoop();
