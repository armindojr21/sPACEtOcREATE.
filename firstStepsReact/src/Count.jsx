import { useState } from "react"

function Count(){
   const [count, setCount] = useState(0)

    const increment = () => {
        setCount(count+1) 
    }
     const decrement = () => {
        setCount(count-1) 
    }
    const reset = () => {
        setCount(count-count)
    }
    return(
        <div className="count-container">
            <p className="count-display">{count}</p>
            <button className="counter-button" onClick={increment}>Add&nbsp;</button>
            <button className="counter-button" onClick={decrement}>Subtract&nbsp;</button>
            <button className="counter-button" onClick={reset}>Reset</button>

        </div>
    )
}
export default Count