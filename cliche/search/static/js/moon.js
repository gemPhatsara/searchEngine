
document.documentElement.classList.remove('no-js'),
gsap.registerPlugin(MotionPathPlugin);
const COLOR_STORAGE_KEY='user-color-scheme';
const COLOR_VAR='--color-mode';
const moonOrSun = document.querySelector('#moon-or-sun');
const darkModeCheckbox=document.querySelector('#toggle-checkbox');
const toggleSlider=document.querySelector('.toggle-slider');

    getCSSCustomProp=b=>{
        let a=getComputedStyle(document.documentElement).getPropertyValue(b);return a.length&&(a=a.replace(/\"|'/g,'').trim()),a
    },
    getCurrentSetting=(b,c,d,e)=>{
        let a=b||localStorage.getItem(d);
        return a?document.documentElement.setAttribute(c,a):a=getCSSCustomProp(e),a
    },
    applyColorSetting=b=>{
        const a=getCurrentSetting(b,'data-user-color-scheme',COLOR_STORAGE_KEY,COLOR_VAR);
        darkModeCheckbox.checked=a==='dark',toggleSlider.classList.contains('with-transition')||(moonOrSun.className=a==='dark'?'moon':'sun',animateSunIn(0),toggleSlider.classList.add('with-transition'))
    },
    toggleColorSetting=()=>{
        let a=localStorage.getItem(COLOR_STORAGE_KEY);
        switch(a){
            case null:a=getCSSCustomProp(COLOR_VAR)==='dark'?'dark':'light';
                break;
            case'light':a='dark';
                break;
            case'dark':a='light';
                break
        }
        return localStorage.setItem(COLOR_STORAGE_KEY,a),a
    };
    darkModeCheckbox.addEventListener('click',a=>{
        animateSunOut(),applyColorSetting(toggleColorSetting())
        changeColor()
    }),
    moonOrSun.addEventListener('click',a=>{
        animateSunOut(),applyColorSetting(toggleColorSetting())
        changeColor()
    });

    function changeColor(){
        if(localStorage.getItem(COLOR_STORAGE_KEY) == 'dark'){
            $('.fa-search').css('color','#ffffff');
        }else{
            $('.fa-search').css('color','#000000');
        }
    }
    applyColorSetting();
    function animateSunIn(a){
        gsap.to('#moon-or-sun',{
            motionPath:{
                path:'#sun-motion-path',
                align:'#sun-motion-path',
                alignOrigin:[.5,.5],
                autoRotate:!1,
                end:.5
            },
            transformOrigin:'50% 50%',
            duration:a,
            immediateRender:!0
        })
        // sessionStorage.setItem("nightMode", "0");
        //     $('body').css('background-image','linear-gradient(hsla(201, 80%, 75%, 1), hsla(164, 97%, 90%, 1), hsla(350, 100%, 96%, 1))');



            // $('.str').hide();
            // $('#moon-or-sun').removeClass("moon").addClass("sun"); //Adds 'a', removes 'b'
    }
    function animateSunOut(){
        gsap.to('#moon-or-sun',{
            motionPath:{
                path:'#sun-motion-path',
                align:'#sun-motion-path',
                alignOrigin:[.5,.5],
                autoRotate:!1,
                start:.5,
                end:1
            },
            transformOrigin:'50% 50%',
            duration:1,
            immediateRender:!0,
            onComplete:()=>{
                const a=moonOrSun.className;
                moonOrSun.className=a==='sun'?'moon':'sun',
                animateSunIn(2)
            }
        })

        // sessionStorage.setItem("nightMode", "1");
        // $('body').css('background-image','linear-gradient(hsla(239, 50%, 20%, 1), hsla(251, 54%, 50%, 1),hsla(290,100%,50%,0.3))');
        // $('.str').show();



        // $('#moon-or-sun').removeClass("sun").addClass("moon"); //Adds 'a', removes 'b'
    }