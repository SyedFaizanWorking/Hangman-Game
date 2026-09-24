


function startJavaScriptFunc() {

    let startbtn = document.getElementById('startBtn')
    let modesForm = document.getElementById('modesform')
    let hintBx = document.getElementById('hintBox')
    let enterbtn = document.getElementById('enterbtn')
    let cover = document.getElementById('startCover')
    let hangmanChar = document.getElementById('hangmanChar')
    let imgChar = document.getElementById('imgChar')
    let correctnotify = document.getElementById('correctnotify')
    let wrongnotify = document.getElementById('wrongnotify')
    let trailsBox = document.getElementById('trailsBox')
    let alphabets = document.querySelectorAll('.alphabets');

    const btncllickSound = new Audio('/static/btnClick.wav')
    const enterBtnSound = new Audio('/static/enterBtn.wav')
    const startGameSound = new Audio('/static/startGame.wav')
    const loseGameSound = new Audio('/static/loseGame.wav')
    const winGameSound = new Audio('/static/winGame.wav')
    const yesSound = new Audio('/static/yes.wav')
    const backgroundSound = new Audio('/static/backgroundSound.mp3')


    // hangmanChar.innerHTML = `<img class="gamecharImg" src="../static/normal.gif" alt="s">`;
    imgChar.src = "/static/normal.gif";
    enterbtn.disabled = true;
    modesForm.disabled = true;
    hintBx.style.display = "none";

    let wordsObjBackend = [];
    let isBackendArrHasLength = false;
    let trails = 0;
    let emptyInputs = [];
    let nonEmptyInputsvalues = [];
    let userTypedInputsvalues = [];
    let wordsMapValue = []
    let isEnterBtnDisabled = true;
    let ismatch = false;
    // let messageOutput = '';
    let currentMode = '0'
    modesForm.value = '0';
    let count = -1;
    let charTopValue = '';




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
            let inputFieldsBox = document.getElementById("inputFieldsBox");
            let hintpara = document.getElementById('hintpara')
            let word = wordsObjBackend.Word;
            let hint = wordsObjBackend.Hint;
            hintBx.style.display = "block";
            let wordsArr = word.split('')

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
                wordsArr.forEach((e, ind) => {
                    if (ind === num1 || ind === num2) {
                        dyInputs += `
  <input name='inputfield_${ind}' id='inputfield_${ind}' inputmode='none'  value='${e}' type='text' class='inputfield_${ind} inputField'>
  
`;


                    }


                    else {

                        dyInputs += `
  <input name='inputfield_${ind}' id='inputfield_${ind}' inputmode='none' value='' type='text' class='inputfield_${ind} inputField'>
  
`;

                    }


                });

                inputFieldsBox.innerHTML = dyInputs;
                hintpara.innerText = hint;
                let emy = []

                const inputNodeList = document.querySelectorAll('.inputField');
                inputNodeList.forEach((e, i) => {


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
        e.preventDefault();
        imgChar.src = "/static/normal.gif";
        setTimeout(() => {
            console.log("show me the setTime Out")
            backgroundSound.currentTime = 0;
            backgroundSound.play();
        }, 500);

        currentMode = '0'

        charTopValue = parseInt(getNestedMediaCssTop(hangmanChar))

        console.log("Hangman TOP:", parseInt(getNestedMediaCssTop(hangmanChar)));

        // hangmanChar.style.top = `${charTopValue}%`
        startGameSound.currentTime = 0;
        startGameSound.play();
        let cover = document.getElementById('startCover')
        cover.classList.add('disabled');
        modesForm.disabled = false;
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

            btncllickSound.currentTime = 0;
            btncllickSound.play();


            if (emptyInputs.length) {
                if (emptyInputs.length !== count + 1) {
                    count++;


                    const inputNodeList = document.querySelectorAll('.inputField');
                    inputNodeList.forEach((e, i) => {




                        if (e.id === emptyInputs[count].id) {
                            e.value = keyEvent.target.innerText.toLowerCase();
                            userTypedInputsvalues.push(keyEvent.target.innerText.toLowerCase());
                            e.blur();
                            console.log("show me the user typed arry", userTypedInputsvalues)









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
        enterBtnSound.currentTime = 0;
        enterBtnSound.play();

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

            if (result.Response_Data.New_Words !== null) {
                if (ismatch) {

                    setTimeout(() => {
                        yesSound.play();
                        yesSound.currentTime = 0;
                    }, 500);

                    console.log("Yes you type correct word")
                    correctnotify.style.display = "flex";
                    setTimeout(() => {
                        correctnotify.style.display = "none";
                    }, 1500);
                } else {
                    wrongnotify.style.display = "flex";
                    setTimeout(() => {
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
                    backgroundSound.pause();
                    hintBx.style.display = "none";
                    emptyInputs = [];
                    nonEmptyInputsvalues = [];
                    userTypedInputsvalues = [];
                    count = -1
                    setTimeout(() => {
                        enterbtn.disabled = true;
                        modesForm.disabled = true;
                        loseGameSound.currentTime = 0;
                        loseGameSound.play();
                        cover.classList.remove('disabled');

                        let ptext = document.querySelectorAll("#paraText,#warningText,#startBtn")
                        console.log("show my loop", ptext)
                        let fstPra = `<img src="../static/angry.png" alt="s" class="d2-img1 d2-img"> Man Die : You Lose! <img src="../static/angry.png" alt="s" class="d2-img1 d2-img">`;
                        let btntext = "Start Again";
                        let wtext = `In which you have only three trais to save the man,But ${result.Response_Data.Message} So Beware for Next Time.`;
                        ptext.forEach((e) => {
                            if (e.id === "paraText") {
                                e.style.fontSize = '22px';
                                e.innerHTML = fstPra
                            }
                            if (e.id === "startBtn") {
                                e.innerText = btntext
                            }
                            if (e.id === "warningText") {
                                e.innerText = wtext
                            }
                        })
                    }, 1000);




                }

                if (result.Response_Data.Win) {
                    backgroundSound.pause();

                    hintBx.style.display = "none";
                    emptyInputs = [];
                    nonEmptyInputsvalues = [];
                    userTypedInputsvalues = [];
                    count = -1
                    setTimeout(() => {
                        enterbtn.disabled = true;
                        modesForm.disabled = true;
                        winGameSound.currentTime = 0;
                        winGameSound.play();
                        cover.classList.remove('disabled');
                        let ptext = document.querySelectorAll("#paraText,#warningText,#startBtn")
                        console.log("show my loop", ptext)
                        let fstPra = `<img src="../static/happy.png" alt="s" class="d2-img1 d2-img">  You Win! <img src="../static/happy.png" alt="s" class="d2-img1 d2-img">`;
                        let btntext = "Start Again";
                        let wtext = ` ${result.Response_Data.Message} So Let's Play Again`;
                        ptext.forEach((e) => {
                            if (e.id === "paraText") {
                                e.style.fontSize = '22px';
                                e.innerHTML = fstPra
                            }
                            if (e.id === "startBtn") {
                                e.innerText = btntext
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
                // hangmanChar.style.top = "65%"
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
                hangmanChar.style.top = `${charTopValue - 4}%`

                imgChar.src = "/static/dead.gif";
            }


            console.log("show me the wordobj", wordsObjBackend)


            // generateInputs()



        } catch (error) {
            console.log("there is some error occurs", error)

        }

    })


}









window.addEventListener('DOMContentLoaded', startJavaScriptFunc);