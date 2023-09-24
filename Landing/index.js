function handleinput(busno){

    document.querySelector('.main-class').style.gridTemplateColumns = "1fr 1fr";
    document.querySelector('.details').style.display = "block";

    fetch(`http://127.0.0.1:80/busno/${parseInt(busno)}`)
        .then(response => response.json())
        .then(json => {
            // const driver = document.querySelector(".drivername");
            // const route = document.querySelector('.route');
            const details_div = document.querySelector('.right_side_content')
            if (json.driver_name) {
                document.querySelector('.driver h2 span').innerHTML = `${busno}`;
                document.querySelector('.drivername').innerHTML = `${json.driver_name}`;
                document.querySelector('.registration').innerHTML = `${json.registration}`;
                document.querySelector('.from').innerHTML = `${json.route.from}`;
                document.querySelector('.to').innerHTML = `${json.route.to}`;
                // route.innerHTML = `From: ${json.route.from}, To: ${json.route.to}`;
            } else {
               alert("something wrong");
            }
        })
        .catch(error => console.error('Error:', error));
}
document.querySelector('.one').addEventListener('click',()=>{
    const value = document.querySelector('.one').value;
    handleinput(value);
});
document.querySelector('.two').addEventListener('click',()=>{
    const value = document.querySelector('.two').value;
    handleinput(value);
});
document.querySelector('.three').addEventListener('click',()=>{
    const value = document.querySelector('.three').value;
    handleinput(value);
});
document.querySelector('.four').addEventListener('click',()=>{
    const value = document.querySelector('.four').value;
    handleinput(value);
});
document.querySelector('.five').addEventListener('click',()=>{
    const value = document.querySelector('.five').value;
    handleinput(value);
});
document.querySelector('.six').addEventListener('click',()=>{
    const value = document.querySelector('.six').value;
    handleinput(value);
});
document.querySelector('.seven').addEventListener('click',()=>{
    const value = document.querySelector('.seven').value;
    handleinput(value);
});
document.querySelector('.eight').addEventListener('click',()=>{
    const value = document.querySelector('.eight').value;
    handleinput(value);
});
document.querySelector('.nine').addEventListener('click',()=>{
    const value = document.querySelector('.nine').value;
    handleinput(value);
});
document.querySelector('.ten').addEventListener('click',()=>{
    const value = document.querySelector('.ten').value;
    handleinput(value);
});
document.querySelector('.track-btn').addEventListener('click',()=>{
    document.querySelector('.inputbox').style.display = 'none';
    document.querySelector('.map').style.display = 'block';
    console.log("23");
});