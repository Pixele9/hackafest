window.onload = function(){

    document.getElementById("btnIniciarSesion").addEventListener("click", iniciarSesion)
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function iniciarSesion()
{
    let user = document.getElementById("user").value;
    let password = document.getElementById("password").value;
    let token = getCookie('csrftoken');

    if(user.length>0 && password.length>0)
    {
        $.ajax({ 
            type: 'POST',
            url: '',
            data: {csrfmiddlewaretoken: token, user:user, password:password},
            success: function(data)
            {
                if(data==1)
                {
                    // PONER EL REDIRECCIONAMIENTO HACIA LOS PERFILES
                    location.href = '../index'
                }
                else
                {
                    alert("Datos incorrectos\nFavor de verificarlos");
                }
            }
         });
    }
    else
    {
        alert("Favor de ingresar tus datos");
    }
}

function getPrediction()
{
    let municipio = document.getElementById("municipio").value;
    let edad = document.getElementById("edad").value;
    let mesEntrega = document.getElementById("mesEntrega").value;
    let genero = document.getElementById("genero").value;
    let ocupacion = document.getElementById("ocupacion").value;
    let token = getCookie('csrftoken');

    console.log(municipio, edad, mesEntrega, genero, ocupacion);

    if(municipio.length>0 && edad.length>0 && mesEntrega.length>0)
    {
        $.ajax({ 
            type: 'POST',
            url: '../getPrediction',
            data: {csrfmiddlewaretoken: token, municipio:municipio, edad:edad, mesEntrega:mesEntrega, genero:genero, ocupacion:ocupacion},
            success: function(data)
            {
                console.log(data);
            }
         });
    }
    else
    {
        alert("Favor de ingresar tus datos");
    }
}

function perfil()
{
    tarjeta = document.getElementById("perfil-ideal");
    tarjeta.style.display="inline";
}

function mensajes()
{
    var token = getCookie('csrftoken');

    $.ajax({ 
        type: 'POST',
        url: '../mensaje/',
        data: {csrfmiddlewaretoken: token},
        success: function(data)
        {
            // console.log(data);
            alert("Mensaje enviado");
        }
     });

}