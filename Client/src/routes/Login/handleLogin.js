import { baseURL } from '../Settings';

// src/routes/Businesses/handleSubmit.js
export function handleLogin(Email, Password,formValid) {
  
  console.log("handleLogin",Email, Password,formValid)

  if (!formValid) {
		const invalidFields = document.querySelectorAll("input:invalid");
		if (invalidFields.length > 0) {
			invalidFields[0].focus();
		}
		return true;
	}
  const LoginData = {
    Email: Email,
    Password: Password
  };

  const queryString = Object.keys(LoginData)
    .map(key => key + '=' + encodeURIComponent(LoginData[key]))
    .join('&');

  const url = baseURL + '/Login/Login?' + queryString; 
  console.log(url)
  fetch(url, {
    method: 'GET'
  })
  .then(response => response.json())
  .then(SessionId => {
    if (SessionId){
      console.log("Save success, SessionId:",SessionId);
      Cookies.set("SessionId", SessionId, { expires: 365 });
      if (Cookies.get("previousLocation")){
        window.location.href = Cookies.get("previousLocation");
      }else{
        window.location.href = "/?s=0";
      }
      // Handle the response data as needed
    }else {
			Cookies.remove("sessionId");
      const formFields = document.querySelectorAll("input");
			formFields[2].focus();
    }
    
  })
  .catch(error => {
    console.error("save error",error);
    // Handle the error as needed
  });
return true
}
