function ajax(url) 
{ 
    req = null; 
    // Procura por um objeto nativo (Mozilla/Safari) 
    if (window.XMLHttpRequest) { 
        req = new XMLHttpRequest(); 
        req.onreadystatechange = processReqChange; 
        req.open("GET",url,true); 
        req.send(null); 
    // Procura por uma versão ActiveX (IE) 
    } else if (window.ActiveXObject) { 
        req = new ActiveXObject("Microsoft.XMLHTTP"); 
        if (req) { 
            req.onreadystatechange = processReqChange; 
            req.open("GET",url,true); 
            req.send(); 
        } 
    } 
}
function processReqChange(){ 
    if (req.readyState == 4) { 
        if (req.status ==200) { 
            var ret = req.responseText;
            var div = document.getElementById('statusMail');
            if (ret=="SUCCESS"){
                div.style.backgroundColor="yellow";
                div.style.color="blue";
                div.innerHTML = "e-mail enviado com SUCESSO !.";
                document.getElementById("button").disabled = "";
                document.getElementById("formMail").reset();
            } else {
                div.style.backgroundColor="yellow";
                div.style.color="red";
                div.innerHTML = "FALHA ao enviar o e-mail.";
                document.getElementById("button").disabled = "";
            }
        } else {
            alert("Houve um problema ao obter os dados:n" + req.statusText); 
        } 
    } 
}