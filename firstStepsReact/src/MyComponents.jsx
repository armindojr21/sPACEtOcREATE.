import { useState } from "react"

function MyComponents(){
    const [name, setName] = useState('Guest')

    function handleNameChange(e)  {
        setName(e.target.value)      
     }

    return (<div>
               <input value={name} onChange={handleNameChange} />
               <p>Name: {name}</p>
            </div>)

}
export default MyComponents