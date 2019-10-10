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
                    location.href = './index'
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