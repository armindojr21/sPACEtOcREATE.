function List(props){
    //fruits.sort((a, b) => a.name.localeCompare(b.name));
    const category = props.category
    const itemList = props.item
    
    
    //itemList.sort((a, b) => a.name.localeCompare(b.name))
    
    const listItems = itemList.map(item =>  <li key={item.id}> 
                                            {item.name} &nbsp;
                                            <b>{item.calories}</b></li>);
    
    return(<>
              <h3> {category}</h3>
              <ol> {listItems}</ol>  
           </>);
}
export default List