const axios = require('axios');
const fs = require('fs');
const path = require('path');
const querystring = require('querystring');

const filePathQueries = path.join(__dirname, 'querytimefarm.txt');

const SLEEP_TIME = 4 * 60 * 60 * 1000 + 5 * 60 * 1000; 
async function main() {
    try {
        const [queriesData] = await Promise.all([
            fs.promises.readFile(filePathQueries, 'utf8')            
        ]);
        
        const queries = queriesData.split('\n').filter(query => query.trim() !== '');
        
        
        await processQueriesLoop(queries);
    } catch (err) {
        console.error('Error reading files:', err);
    }
}

async function processQueriesLoop(queries) {
    while (true) {
        await processQueriesSequentially(queries, 0);
        console.log(`Nghỉ ${SLEEP_TIME / 1000 / 60} phút trước khi tiếp tục vòng lặp...`);
        await sleep(SLEEP_TIME);
    }
}

async function processQueriesSequentially(queries, index) {
    if (index >= queries.length) {
        console.log('Tất cả tài khoản đã được xử lý.');
        return;
    }

    const query = queries[index];
    
    try {
        await sendRequest(query.trim());
    } catch (error) {
        console.error('Lỗi xử lý:', error);
    }
//    await sleep(3000);  
    await processQueriesSequentially(queries, index + 1);
}

async function sendRequest(payload) {
    const url = 'https://tg-bot-tap.laborx.io/api/v1/auth/validate-init';

    try {
        const response = await axios.post(url, payload, {
            headers: {
                'Content-Type': 'text/plain;charset=UTF-8',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'Origin': 'https://tg-tap-miniapp.laborx.io',
                'Referer': 'https://tg-tap-miniapp.laborx.io/',
                'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            }
            
        });

        const parsedPayload = querystring.parse(payload);

        const user = JSON.parse(decodeURIComponent(parsedPayload.user));
        const firstName = user.first_name;
        const lastName = user.last_name;

        const balance = response.data.balanceInfo.balance;
        const level = response.data.info.level;

        console.log(`======Tài khoản ${firstName} ${lastName}======`);
        console.log(`Balance: ${balance}`);
        console.log(`Level: ${level}`);

        const token = response.data.token;
        await getFarmingInfo(token);
    } catch (error) {
        console.error(`Error for payload: ${payload}`);
        console.error(error);
    }
}

async function getFarmingInfo(token) {
    const url = 'https://tg-bot-tap.laborx.io/api/v1/farming/info';

    try {
        const response = await axios.get(url, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            }
           
        });

        const farmingInfo = response.data;
        const currentTime = new Date();
        const farmingEndTime = farmingInfo.activeFarmingStartedAt 
            ? new Date(new Date(farmingInfo.activeFarmingStartedAt).getTime() + farmingInfo.farmingDurationInSec * 1000) 
            : null;

        console.log(`Kiểm tra farming...`);

        if (!farmingInfo.activeFarmingStartedAt) {
            await startFarming(token);
        } else if (farmingEndTime && farmingEndTime < currentTime) {
            await finishFarming(token);
        }
    } catch (error) {
        console.error('Không thể kiểm tra dữ liệu:');
        console.error(error);
    }
}

async function startFarming(token) {
    const url = 'https://tg-bot-tap.laborx.io/api/v1/farming/start';

    try {
        await axios.post(url, {}, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            }
            
        });
        console.log('Bắt đầu farm...');
    } catch (error) {
        console.error('Không thể bắt đầu farm');
        console.error(error);
    }
}

async function finishFarming(token) {
    const url = 'https://tg-bot-tap.laborx.io/api/v1/farming/finish';

    try {
        const response = await axios.post(url, {}, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            }
            
        });

        const balance = response.data.balance;
        console.log(`Claim thành công. Balance: ${balance}`);
        await startFarming(token);
    } catch (error) {
        console.error('Không thể claim:');
        console.error(error);
    }
}
  
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

main();
