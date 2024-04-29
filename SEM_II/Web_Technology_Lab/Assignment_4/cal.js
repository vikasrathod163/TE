
let out = document.getElementById("output");

function appendVal(val){
    out.value += val;
}

function clearoutput(){
    out.value = "";
}

function calculate(){
    

    try {
        let res = eval(out.value);

        if(isNaN(res) || !isFinite(res)){
            throw "Invalid";
        }
        out.value = res;
    } catch (error) {
        alert("Invalid Expression");
        out.value = "";
    }
    
}

function square(){
    

    try{
        let ans = (out.value * out.value);
        if(isNaN(ans)){
            throw("Invalid");
        }
        out.value = ans;
    }
    catch(err){
        alert("Invalid");
        out.value = "";
    }
}

function cube(){
       
    
    try{
        let ans = (out.value * out.value * out.value);
        if(isNaN(ans)){
            throw("Invalid");
        }
        out.value = ans;
    }
    catch(err){
        alert("Invalid");
        out.value = "";
    }
}

function sroot(){

    try{
        let ans = Math.sqrt(out.value);
        if(isNaN(ans)){
            throw("Invalid");
        }
        out.value = ans;
    }
    catch(err){
        alert("Invalid");
        out.value = "";
    }
}

function fact(){
    

    try{
        let fact = 1;
        for(let i = out.value;i >= 1;i--){
            fact = fact * i;
        }

        if(isNaN(fact)){
            throw("Invalid.");
        }
        out.value = fact;

    }
    catch(err){
        alert("Invalid Expression");
        out.value = "";
    }
}


function ac(){
    out.value = "Not Defined Yet!";
}