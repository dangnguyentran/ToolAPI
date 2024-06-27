const fs = require('fs'),
    axios = require('axios'),
    path = require('path'),
    tokenPath = path.join(__dirname, 'tokenmobiversebigmouth97.txt'),
    authToken = 'Bearer ' + fs.readFileSync(tokenPath, 'utf8').trim(),
    baseURL = 'https://mobiverse-backend-prod-c4gljf5eva-uc.a.run.app',
    headers = {
        'Authorization': authToken,
        'Content-Type': 'application/json'
    };

function getFormattedDateTime() {
    const now = new Date(),
        hours = now.getHours().toString().padStart(2, '0'),
        minutes = now.getMinutes().toString().padStart(2, '0'),
        seconds = now.getSeconds().toString().padStart(2, '0'),
        day = now.getDate().toString().padStart(2, '0'),
        month = (now.getMonth() + 1).toString().padStart(2, '0'),
        year = now.getFullYear();
    return `[${hours}:${minutes}:${seconds}, ${day}/${month}/${year}]`;
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function getUserInfo() {
    try {
        const response = await axios.get(baseURL + '/users', { headers });
        return response.data;
    } catch (error) {
        console.error(getFormattedDateTime() + ' Gagal lấy thông tin người dùng: ' + (error.response ? error.response.data.message : error.message));
        return null;
    }
}

async function mineGold(mineIndex) {
    try {
        const response = await axios.patch(baseURL + '/users/mintPool?mineIndex=' + mineIndex, {}, { headers });
        return response.data;
    } catch (error) {
        console.error(getFormattedDateTime() + ` Lỗi khai thác mỏ ${mineIndex}: ` + (error.response ? error.response.data.message : error.message));
        return null;
    }
}

async function activateFever() {
    const feverURL = baseURL + '/fever/activate';
    try {
        const response = await axios.post(feverURL, {}, { headers }),
            data = response.data;
        if (data.success) {
            console.log(getFormattedDateTime() + ' Kích hoạt Fever thành công');
        } else {
            console.log(getFormattedDateTime() + ' Lỗi kích hoạt Fever');
            console.log('Response Error: ' + JSON.stringify(response.data));
        }
    } catch (error) {
        console.error(getFormattedDateTime() + ' Lỗi kích hoạt Fever: ' + (error.response ? error.response.data.message : error.message));
        console.error('Response Error: ' + JSON.stringify(error.response ? error.response.data : error.message));
    }
}

async function spinWheel() {
    const spinURL = baseURL + '/wheel/spin';
    try {
        const response = await axios.post(spinURL, {}, { headers }),
            { newUserData, prize, prizeValue } = response.data;
        console.log(getFormattedDateTime() + ` Quay thành công | Còn lại Kim cương: ${newUserData.diamond} | Phần thưởng: ${prizeValue} ${prize.name}`);
        if (newUserData.diamond > 0) {
            await spinWheel();
        } else {
            console.log(getFormattedDateTime() + ' Kim cương bằng 0, không thể quay thêm.');
        }
    } catch (error) {
        console.error(getFormattedDateTime() + ' Lỗi quay: ' + (error.response ? error.response.data.message : error.message));
    }
}

async function runBot() {
    const userInfo = await getUserInfo();
    if (!userInfo) return;

    console.log('\n==================================================');
    console.log(getFormattedDateTime() + ' ID: ' + userInfo.id);
    console.log(getFormattedDateTime() + ' Cấp độ: ' + userInfo.level);
    console.log(getFormattedDateTime() + ' EXP: ' + userInfo.exp);
    console.log(getFormattedDateTime() + ' Token: ' + userInfo.token);
    console.log(getFormattedDateTime() + ' Số lượng kim cương: ' + userInfo.diamond);
    console.log('==================================================\n');

    await delay(1000);

    while (true) {
        const mineIndex = Math.floor(Math.random() * 50) + 1;
        console.log(getFormattedDateTime() + ' Đang tìm kiếm mỏ....');
        await delay(1000);
        console.log(getFormattedDateTime() + ' Mỏ được chọn: ' + mineIndex);
        await delay(1000);
        console.log(getFormattedDateTime() + ` Đang cố gắng khai thác mỏ ${mineIndex}\n`);
        await delay(1000);

        while (true) {
            const mineResult = await mineGold(mineIndex);
            if (mineResult) {
                const currentAmount = Math.round(mineResult.currentAmount * 100) / 100,
                    maxAmount = Math.round(mineResult.maxAmount * 100) / 100,
                    rewardValue = Math.round(mineResult.rewardValue * 100) / 100,
                    level = mineResult.level,
                    diamond = mineResult.diamond;
                console.log(getFormattedDateTime() + ` Mỏ ${mineIndex} | Số lượng: ${currentAmount}/${maxAmount} | Phần thưởng: ${rewardValue} | Cấp độ: ${level} | Kim cương: ${diamond}`);
                if (currentAmount === 0) {
                    console.log(getFormattedDateTime() + ` Mỏ ${mineIndex} đã hết. Tìm mỏ khác\n`);
                    break;
                }
                const feverActive = mineResult.feverUpdateStatus ? mineResult.feverUpdateStatus.success : false;
                if (!feverActive) {
                    console.log(getFormattedDateTime() + ' Fever sẵn có! Đang kích hoạt...');
                    await activateFever();
                    if (mineResult.feverUpdateStatus) {
                        mineResult.feverUpdateStatus.success = true;
                    }
                    if (mineResult.diamond > 0) {
                        await spinWheel();
                    } else {
                        console.log(getFormattedDateTime() + ' Kim cương bằng 0, không thể quay thêm.');
                    }
                }
            } else {
                console.log(getFormattedDateTime() + ' Bỏ qua.\n');
                break;
            }
            await new Promise(resolve => setTimeout(resolve, 10000));
        }
        await new Promise(resolve => setTimeout(resolve, 3000));
    }
}

runBot();
