document.getElementById("excavation").addEventListener("change", toggle_options1);


function toggle_options1() {
    if (document.getElementById("excavation").checked === true){
        document.getElementById("scanned").disabled,true;
        console.log("its on");
        }}
