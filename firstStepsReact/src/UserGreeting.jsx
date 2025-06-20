 

function UserGreeting(props){
    //if (props.isLogged){
       // return(
    //    <h2>Welcome back {props.username}.</h2>)
   // }
   // else{
     //   return(
     //   <h2>{props.username}, please log in</h2>
      //  ) } 
    //return(
    //props.isLogged ? <h2 className="welcome-message">Welcome back {props.username}.</h2> :
      //               <h2 className="login-prompt">{props.username}, please log in</h2>
    //)
    const welcome_message = <h2 className="welcome-message">Welcome back {props.username}.</h2> 
    const login_prompt = <h2 className="login-prompt">Please log in.</h2>
    return (props.isLogged ? 
        welcome_message :
        login_prompt

    ) 


}

export default UserGreeting