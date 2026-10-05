


function startJavaScriptFunc() {

    let startbtn = document.getElementById('startBtn')
    let hintBx = document.getElementById('hintBox')
    let enterbtn = document.getElementById('enterbtn')
    let translateBtn = document.getElementById('translateBtn')
    let crossbtn = document.getElementById('crossbtn')
    let hintBulb = document.getElementById('hintBulb')
    let cover = document.getElementById('startCover')
    let hangmanChar = document.getElementById('hangmanChar')
    let imgChar = document.getElementById('imgChar')
    let correctnotify = document.getElementById('correctnotify')
    let wrongnotify = document.getElementById('wrongnotify')
    let trailsBox = document.getElementById('trailsBox')
    let trailsBoxMainDiv = document.getElementById('trailsBoxMainDiv')
    let incrementDecrement = document.getElementById('incrementDecrement')
    let alphabets = document.querySelectorAll('.alphabets');

    const btncllickSound = new Audio('/static/btnClick.wav')
    const enterBtnSound = new Audio('/static/enterBtn.wav')
    const startGameSound = new Audio('/static/startGame.wav')
    const loseGameSound = new Audio('/static/loseGame.wav')
    const winGameSound = new Audio('/static/winGame.wav')
    const yesSound = new Audio('/static/yes.wav')
    const backgroundSound = new Audio('/static/backgroundSound.mp3')

    const dropBtn = document.getElementById("timeBox");
    const dropdownMenu = document.getElementById("dropdownMenu");
    const timeforms = document.querySelectorAll(".time-option-items");

    let modesForm = document.getElementById('modesform');
    const modesDropdownBtn = document.getElementById("modesDropdownBtn");
    const modesDropdownMenu = document.getElementById("modesDropdownMenu");
    const modesOptionsList = document.querySelectorAll(".modes-option-item");

    let volumeBox = document.getElementById('volumeBox');
    let volBoxArrowIcon = document.getElementById('volBoxArrowIcon');
    let speakerIconsDiv = document.getElementById('speakerIconsDiv');


    imgChar.src = "/static/normal.gif";
    enterbtn.disabled = true;
    hintBx.style.display = "none";
    trailsBoxMainDiv.style.display = "none";

    cover.style.backgroundImage = "url('/static/mainModal.png')";

    correctnotify.style.backgroundImage = "url('/static/notify.png')";
    wrongnotify.style.backgroundImage = "url('/static/notify.png')";

    let wordsObjBackend = [];
    let isBackendArrHasLength = false;
    let trails = 0;
    // let myNumber = 0;
    let emptyInputs = [];
    let nonEmptyInputsvalues = [];
    let userTypedInputsvalues = [];
    let wordsMapValue = []
    let isEnterBtnDisabled = true;
    let ismatch = false;
    let currentMode = '0'
    let count = -1;
    let charTopValue = '';
    let isSoundMute = false;
    const modeLabels = { '0': 'Easy', '1': 'Medium', '2': 'Hard' };
    const timeArr = [120, 180, 300, 600];

    // const timeshow = ['1:30']
    dropBtn.style.backgroundImage = "url('/static/timerBtn.png')"
    dropBtn.classList.add("d-none");
    modesDropdownBtn.classList.add('pointer-none')
    volumeBox.classList.add('volumeBox-none')
    modesForm.value = '0';
    timeforms.value = '0';
    // hintBx.style.display = "none";
    hintBulb.style.display = "none";

    let valuePoints = 6;

    modesDropdownBtn.addEventListener("click", (event) => {
        modesDropdownMenu.classList.toggle("open");
        event.stopPropagation();
    });

    modesOptionsList.forEach(item => {
        item.addEventListener("click", (event) => {
            const targetValue = event.target.dataset.value;
            modesDropdownBtn.textContent = modeLabels[targetValue];
            modesForm.value = targetValue;
            modesForm.dispatchEvent(new Event('change', { bubbles: true }));
            modesDropdownMenu.classList.remove("open");
        });
    });

    window.addEventListener("click", () => {
        modesDropdownMenu.classList.remove("open");
    });

    let intervalId = null;
    function timeCountDown(timeValue, btnClk = false) {
        let timeBoxText = document.getElementById('timeBoxText')
        let firstIntervalid = '';
        let counter = timeValue;

        if (intervalId) {
            clearInterval(intervalId);
            counter = timeValue;
        }



        intervalId = setInterval((e) => {
            firstIntervalid = intervalId
            const minutes = Math.floor(counter / 60);
            let seconds = counter % 60;

            if (seconds < 10) {
                let formattedSeconds = String(seconds).padStart(2, '0');
                seconds = formattedSeconds
            }

            timeBoxText.innerHTML = `${minutes}:${seconds}`

            if (counter === 0) {
                // console.log("show counter zero")
                clearInterval(intervalId)
                intervalId = null;
                backgroundSound.pause();
                hintBx.style.display = "none";
                emptyInputs = [];
                nonEmptyInputsvalues = [];
                userTypedInputsvalues = [];
                count = -1
                createProgressBar(trails)
                setTimeout(() => {
                    trails = 0;
                    trailsBox.innerText = trails
                    if (trails === 0) {
                        hangmanChar.style.top = `${charTopValue - 4}%`
                        imgChar.src = "/static/dead.gif";
                    }
                    enterbtn.disabled = true;
                    modesDropdownBtn.classList.add('pointer-none')
                    dropBtn.classList.add("d-none");
                    if (!isSoundMute) {
                        loseGameSound.currentTime = 0;
                        loseGameSound.play();
                    }
                    cover.classList.remove('disabled');
                    cover.style.gap = "5px";
                    volumeBox.classList.add('volumeBox-none')
                    let ptext = document.querySelectorAll("#tt,#paraText,#warningText,#startBtn")
                    console.log("show my loop", ptext)
                    let ttbox = `<span>Time Up!</span>`;
                    let fstPra = `
                    
                    <img src="../static/angry.png" alt="s" class="d2-img1 d2-img"> Man Die : You Lose! <img src="../static/angry.png" alt="s" class="d2-img1 d2-img">`;
                    // let btntext = "Play Again";
                    // let wtext = `In which you have only three trais and must be completed to given time to save the man, So Beware for Next Time.`;
                    let playAgainSpan = document.getElementById("buttonSpanTag")


                    let wtext = `Let's Play!`;
                    ptext.forEach((e) => {
                        if (e.id === "tt") {
                            e.style.marginBottom = "-18px";
                            // e.style.fontSize = '18px';
                            e.innerHTML = ttbox
                        }
                        if (e.id === "paraText") {
                            // e.style.fontSize = '18px';
                            e.innerHTML = fstPra
                        }
                        if (e.id === "startBtn") {
                            playAgainSpan.innerText = "Play Again";
                        }
                        if (e.id === "warningText") {
                            e.innerText = wtext
                        }
                    })
                }, 1000);





            }
            counter--

            return intervalId;
        }, 1000);




    }


    timeforms.forEach((items) => {
        items.addEventListener("click", (itemClick) => {
            const itemsData = parseInt(itemClick.target.dataset.value)
            timeCountDown(timeArr[itemsData])
            // clearInterval(intervalId)

        })
    })



    dropBtn.addEventListener("click", (event) => {
        dropdownMenu.classList.toggle("show");
        event.stopPropagation();
    });

    window.addEventListener("click", () => {
        if (dropdownMenu.classList.contains("show")) {
            dropdownMenu.classList.remove("show");
        }
    });


    volBoxArrowIcon.addEventListener("click", (e) => {
        let parent = e.target.parentElement.offsetParent
        parent.classList.toggle('volumeBox-toggle')
        setTimeout(() => {
            parent.classList.remove('volumeBox-toggle')
        }, 5000);
        e.stopPropagation();
    })

    speakerIconsDiv.addEventListener("click", (e) => {
        const fullVol = e.currentTarget.querySelector('.fullVol');
        const muteVol = e.currentTarget.querySelector('.muteVol');
        fullVol.classList.toggle('d-none');
        muteVol.classList.toggle('d-visible');
        if (!fullVol.classList.contains('d-visible')) {
            backgroundSound.pause();
            isSoundMute = true;

        }
        if (!fullVol.classList.contains('d-none')) {
            backgroundSound.currentTime = 0;
            backgroundSound.play();
            isSoundMute = false;
        }
    })


    function generateInputs() {
        enterbtn.disabled = true;
        count = -1;
        emptyInputs = [];
        wordsMapValue = [];
        userTypedInputsvalues = [];
        nonEmptyInputsvalues = [];
        if (trails === 3) {
            hangmanChar.style.top = `${charTopValue}%`
        }
        if (isBackendArrHasLength === true) {
            hintBx.style.backgroundImage = "url('/static/hintBoard.png')";
            let inputFieldsBox = document.getElementById("inputFieldsBox");
            let hintpara = document.getElementById('hintpara')
            let word = wordsObjBackend.Word;
            let hint = wordsObjBackend.Hint;
            hintBx.style.display = "none";
            let wordsArr = word.split('')
            console.log("---------------show me the word arrr", wordsArr)
            const maxRange = wordsArr.length;
            const num1 = Math.floor(Math.random() * maxRange);
            const validOptionsForNum2 = [];
            for (let i = 0; i < maxRange; i++) {
                if (Math.abs(i - num1) >= 2) {
                    validOptionsForNum2.push(i);
                }
            }
            const randomIndex = Math.floor(Math.random() * validOptionsForNum2.length);
            const num2 = validOptionsForNum2[randomIndex];
            if (wordsArr.length) {
                let dyInputs = "";
                inputFieldsBox.style.backgroundImage = "url('/static/inputBoxframe.png')";
                wordsArr.forEach((e, ind) => {
                    if (ind === num1 || ind === num2) {
                        dyInputs += `
  <input name='inputfield_${ind}' id='inputfield_${ind}' onkeydown="event.preventDefault();" inputmode='none'  value='${e}' type='text' class='inputfield_${ind} inputField'>
  
`;

                    }

                    else {

                        dyInputs += `
  <input name='inputfield_${ind}' id='inputfield_${ind}' onkeydown="event.preventDefault();" inputmode='none' value='' type='text' class='inputfield_${ind} inputField'>
  
`;

                    }


                });

                inputFieldsBox.innerHTML = dyInputs;
                hintpara.style.textAlign = "start";
                hintpara.innerText = hint;
                let emy = []
                const inputNodeList = document.querySelectorAll('.inputField');
                inputNodeList.forEach((e, i) => {
                    e.style.backgroundImage = "url('/static/input_field_frame.png')";
                    if (e.value === '') {
                        emy.push(e)
                        emptyInputs.push(e)
                        wordsMapValue.push("")
                    } else {
                        nonEmptyInputsvalues.push(e.value)
                        wordsMapValue.push(e.value)
                    }
                    if (emy.length) {
                        if (e.id === emy[0].id) {
                            e.focus();
                        }
                    }
                })
            }

        }


    }

    // this function is used for get the top position of character is css 
    function getNestedMediaCssTop(element) {
        let result = null;

        function searchRules(rules) {
            for (const rule of rules) {
                if (rule.type === CSSRule.MEDIA_RULE) {
                    if (window.matchMedia(rule.conditionText).matches) {
                        searchRules(rule.cssRules);
                    }
                    continue;
                }

                if (rule.cssRules && rule.cssRules.length) {
                    searchRules(rule.cssRules);
                }

                if (
                    rule.selectorText &&
                    rule.selectorText.includes(".hangman-character-div") &&
                    rule.style
                ) {
                    const top = rule.style
                        .getPropertyValue("top")
                        .trim();
                    if (/^-?\d*\.?\d+%$/.test(top)) {
                        result = top;
                    }
                }
            }
        }

        for (const sheet of document.styleSheets) {
            try {
                if (sheet.cssRules) {
                    searchRules(sheet.cssRules);
                }
            } catch (error) {

            }
        }

        return result;
    }

    startbtn.addEventListener('click', async (e) => {
        if (intervalId) {
            clearInterval(intervalId);
        }
        timeCountDown(timeArr[0])
        e.preventDefault();
        hintBulb.style.display = "flex";
        trailsBoxMainDiv.style.display = "flex";
        volumeBox.classList.remove('volumeBox-none')
        dropBtn.classList.remove("d-none");
        imgChar.src = "/static/normal.gif";
        if (!isSoundMute) {
            setTimeout(() => {
                console.log("show me the setTime Out")
                backgroundSound.currentTime = 0;
                backgroundSound.play();
            }, 500);
            startGameSound.currentTime = 0;
            startGameSound.play();
        }

        currentMode = '0'
        charTopValue = parseInt(getNestedMediaCssTop(hangmanChar))
        let cover = document.getElementById('startCover')
        cover.classList.add('disabled');
        modesDropdownBtn.classList.remove('pointer-none')
        emptyInputs = [];


        try {
            let data = await fetch('/start-game', {
                method: "POST",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify('0')
            })

            let result = await data.json();
            trails = result.Response_Data.Trails
            trailsBox.innerText = trails;
            // myNumber = trails;
            createProgressBar(trails)
            wordsObjBackend = result.Response_Data.Words;
            isBackendArrHasLength = true;
            console.log("show me the ------- startAgain Value", result);
            modesForm.value = '0';
            generateInputs()
        } catch (error) {
            console.log("Show me the Error", error)
        }


    })

    modesForm.addEventListener("change", async (e) => {

        let val = e.target.value;
        currentMode = e.target.value;
        try {
            let data = await fetch('/game-modes', {
                method: "POST",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(val)
            })

            let result = await data.json();
            trails = result.Response_Data.Trails
            trailsBox.innerText = trails;
            wordsObjBackend = result.Response_Data.Words;
            isBackendArrHasLength = true;
            generateInputs()
            console.log("show me the result", result)
        } catch (error) {
            console.log("Show me the Error", error)
            isBackendArrHasLength = false;
        }

    })

    alphabets.forEach((btns) => {
        btns.addEventListener('click', (keyEvent) => {
            if (!isSoundMute) {
                btncllickSound.currentTime = 0;
                btncllickSound.play();
            }
            if (emptyInputs.length) {
                if (emptyInputs.length !== count + 1) {
                    count++;
                    const inputNodeList = document.querySelectorAll('.inputField');
                    inputNodeList.forEach((e, i) => {
                        if (e.id === emptyInputs[count].id) {
                            e.value = keyEvent.target.innerText.toLowerCase();
                            userTypedInputsvalues.push(keyEvent.target.innerText.toLowerCase());
                            console.log("show my the userTyed Array", userTypedInputsvalues, count)
                            e.blur();
                            inputNodeList.forEach((nxte) => {
                                if (emptyInputs.length !== count + 1) {
                                    if (nxte.id === emptyInputs[count + 1].id) {
                                        console.log("gidf")
                                        nxte.focus()
                                    }
                                }
                            })
                        }
                    })

                }
                if (emptyInputs.length === count + 1) {
                    console.log("length is equal")
                    enterbtn.disabled = false;
                    isEnterBtnDisabled = false;
                }
            }
        })
    })

    crossbtn.addEventListener('click', (e) => {
        // console.log("show me the click", e)
        if (emptyInputs.length) {
            if (emptyInputs.length !== count - 1) {

                const inputNodeList = document.querySelectorAll('.inputField');
                // console.log("userTypedInputsvalues.length", emptyInputs)
                if (userTypedInputsvalues.length > 0) {
                    inputNodeList.forEach((e, i) => {
                        if (e.id === emptyInputs[count].id) {
                            // e.value = keyEvent.target.innerText.toLowerCase();
                            userTypedInputsvalues.pop();
                            e.value = ''
                            console.log("show my the userTyed Array", userTypedInputsvalues, count, emptyInputs)
                            e.focus();
                            // e.style.color = "green";
                            enterbtn.disabled = true;
                            isEnterBtnDisabled = true;

                        }
                    })
                    count--;
                } else {
                    console.log("emptyInputs", emptyInputs, count)
                    inputNodeList.forEach((e, i) => {
                        if (e.id === emptyInputs[count + 1].id) {
                            e.focus();
                        }
                    })
                }

            }
            if (emptyInputs.length === count - 1) {
                console.log("length is equal")
                enterbtn.disabled = false;
                isEnterBtnDisabled = false;
            }
        }
    })

    hintBulb.addEventListener("click", (e) => {
        hintBx.style.display = "flex";
        hintBulb.style.display = "none";
    })

    let hintParaEng = true;
    translateBtn.addEventListener("click", (e) => {
        hintParaEng = !hintParaEng;
        if (hintParaEng) {
            let engHint = wordsObjBackend.Hint;
            hintpara.innerText = engHint;
            hintpara.style.textAlign = "start";

        } else {
            let urduHint = wordsObjBackend.UrduHint;
            hintpara.innerText = urduHint;
            hintpara.style.textAlign = "end";

        }
    });

    enterbtn.addEventListener('click', async (event) => {
        let combinedArry = []
        let arr2Index = 0;
        const arr3 = wordsMapValue.map((char) => {
            if (char === "" && arr2Index < userTypedInputsvalues.length) {
                const replacement = userTypedInputsvalues[arr2Index];
                arr2Index++;
                return replacement;
            }
            return char;
        });
        combinedArry = arr3;
        if (!isSoundMute) {
            enterBtnSound.currentTime = 0;
            enterBtnSound.play();
        }

        try {
            let data = await fetch('/user-data', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ combinedArry, "Current_Mode": currentMode })
            })
            let result = await data.json()
            console.log("show me the request result", result)
            ismatch = result.Response_Data.Match;
            trails = result.Response_Data.Trails
            trailsBox.innerText = trails;
            createProgressBar(trails)
            hintBulb.style.display = "flex";

            if (result.Response_Data.New_Words !== null) {
                if (ismatch) {
                    if (!isSoundMute) {
                        setTimeout(() => {
                            yesSound.play();
                            yesSound.currentTime = 0;
                        }, 500);
                    }

                    let wrightpoints = document.getElementById("wrightpoints");
                    wrightpoints.innerText = valuePoints - trails;
                    console.log("Yes you type correct word")
                    incrementDecrement.classList.add('d-visible');
                    incrementDecrement.innerText = "+1";
                    incrementDecrement.style.color = "#28530c";
                    correctnotify.style.display = "flex";

                    setTimeout(() => {
                        incrementDecrement.classList.remove('d-visible');
                        correctnotify.style.display = "none";
                    }, 1500);
                } else {
                    wrongnotify.style.display = "flex";
                    let wrongpoints = document.getElementById("wrongpoints");
                    wrongpoints.innerText = valuePoints - trails;
                    incrementDecrement.classList.add('d-visible');
                    incrementDecrement.innerText = "-1";
                    incrementDecrement.style.color = "red";
                    console.log("show increment decrement", incrementDecrement)
                    setTimeout(() => {
                        incrementDecrement.classList.remove('d-visible');
                        wrongnotify.style.display = "none";
                    }, 1500);
                    console.log("No the Word Are Not Match")
                }
                wordsObjBackend = result.Response_Data.New_Words
                isBackendArrHasLength = true;
                generateInputs()
            } else {
                isBackendArrHasLength = false;
                wordsObjBackend = null
                if (result.Response_Data.Lose) {
                    if (intervalId) {
                        clearInterval(intervalId);
                    }
                    backgroundSound.pause();
                    hintBx.style.display = "none";
                    emptyInputs = [];
                    nonEmptyInputsvalues = [];
                    userTypedInputsvalues = [];
                    count = -1
                    setTimeout(() => {
                        enterbtn.disabled = true;
                        modesDropdownBtn.classList.add('pointer-none')
                        dropBtn.classList.add("d-none");
                        if (!isSoundMute) {
                            loseGameSound.currentTime = 0;
                            loseGameSound.play();
                        }

                        cover.classList.remove('disabled');
                        cover.style.gap = '15px';
                        volumeBox.classList.add('volumeBox-none')
                        let ttdiv = document.getElementById('tt');
                        ttdiv.style.display = "none";
                        let ptext = document.querySelectorAll("#paraText,#warningText,#startBtn")
                        console.log("show my loop", ptext)
                        let fstPra = `<img src="../static/angry.png" alt="s" class="d2-img1 d2-img"> Man Die : You Lose! <img src="../static/angry.png" alt="s" class="d2-img1 d2-img">`;
                        let btntext = "Play Again";
                        let playAgainSpan = document.getElementById("buttonSpanTag")
                        let wtext = `Let's Play`;
                        ptext.forEach((e) => {
                            if (e.id === "paraText") {
                                // e.style.fontSize = '18px';
                                e.innerHTML = fstPra
                            }
                            if (e.id === "startBtn") {
                                // e.innerText = btntext
                                playAgainSpan.innerText = btntext
                            }
                            if (e.id === "warningText") {
                                e.innerText = wtext
                            }
                        })
                    }, 1000);

                }

                if (result.Response_Data.Win) {
                    if (intervalId) {
                        clearInterval(intervalId);
                    }
                    backgroundSound.pause();
                    hintBx.style.display = "none";
                    emptyInputs = [];
                    nonEmptyInputsvalues = [];
                    userTypedInputsvalues = [];
                    count = -1
                    trails = 6;
                    trailsBox.innerText = trails;
                    let playAgainSpan = document.getElementById("buttonSpanTag")
                    createProgressBar(trails)
                    setTimeout(() => {
                        enterbtn.disabled = true;
                        dropBtn.classList.add("d-none");
                        modesDropdownBtn.classList.add('pointer-none')
                        if (!isSoundMute) {
                            winGameSound.currentTime = 0;
                            winGameSound.play();
                        }
                        cover.classList.remove('disabled');
                        cover.style.gap = '15px';
                        volumeBox.classList.add('volumeBox-none')
                        let ttdiv = document.getElementById('tt');
                        ttdiv.style.display = "none";
                        let ptext = document.querySelectorAll("#paraText,#warningText,#startBtn")
                        console.log("show my loop", ptext)
                        let fstPra = `<img src="../static/happy.png" alt="s" class="d2-img1 d2-img">  You Win! <img src="../static/happy.png" alt="s" class="d2-img1 d2-img">`;
                        hangmanChar.style.top = `${charTopValue}%`
                        imgChar.src = "/static/happy.gif";
                        let btntext = "Play Again";
                        let wtext = `Let's Play`;
                        ptext.forEach((e) => {
                            if (e.id === "paraText") {
                                // e.style.fontSize = '18px';
                                e.innerHTML = fstPra
                            }
                            if (e.id === "startBtn") {
                                playAgainSpan.innerText = btntext
                            }
                            if (e.id === "warningText") {
                                e.innerText = wtext
                            }
                        })
                    }, 1000);




                }





            }

            console.log("show me the trails : ", trails)
            if (trails === 5) {
                hangmanChar.style.top = `${charTopValue}%`
                imgChar.src = "/static/happy.gif";
            }

            if (trails === 3) {
                hangmanChar.style.top = `${charTopValue}%`
                imgChar.src = "/static/normal.gif";
            }

            if (trails === 2) {
                hangmanChar.style.top = `${charTopValue - 1}%`
                imgChar.src = "/static/scary.gif";
            }
            if (trails === 1) {
                // hangmanChar.style.top = "63%"
                hangmanChar.style.top = `${charTopValue - 2}%`
                imgChar.src = "/static/cry.gif";
            }
            if (trails === 0) {
                // hangmanChar.style.top = "60%"
                hangmanChar.style.top = `${charTopValue - 4}% `;
                imgChar.src = "/static/dead.gif";
            }
            console.log("show me the wordobj", wordsObjBackend)
        } catch (error) {
            console.log("there is some error occurs", error)
        }

    })



    function createProgressBar(myNumber) {

        const maxNumber = 6;
        let percentage = (myNumber / maxNumber) * 100;
        percentage = Math.max(0, Math.min(100, percentage));
        const bar = document.querySelector('.progress-bar');
        const labelSpan = document.getElementById('bar-label');
        function get3DColor(num) {
            switch (num) {
                case 1:
                    labelSpan.innerText = "Loss";
                    return '#ff4d4d';
                case 2:
                    labelSpan.innerText = "Loss";
                    return '#ff7675';
                case 3:
                    labelSpan.innerText = "Play";
                    return '#ffcd03';
                case 4:
                    labelSpan.innerText = "+2 Win";
                    return '#ffcc00';
                case 5:
                    labelSpan.innerText = "+1 Win";
                    return '#addf56';
                case 6:
                    labelSpan.innerText = "Win";
                    return '#13c219';
                default:
                    return '#e0e0e0';
            }
        }

        bar.style.width = percentage + '%';
        bar.style.backgroundColor = get3DColor(myNumber);

    }


}









window.addEventListener('DOMContentLoaded', startJavaScriptFunc);