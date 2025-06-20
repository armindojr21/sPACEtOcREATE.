
function Food(){
    const food1 = 'Apple'
    const food2 = 'Orange'
    return(
        <ul>
            <li>Banana</li>
            <li>{food1}</li>
            <li>{food2.toLocaleUpperCase()}</li>
        </ul>)

}
export default Food