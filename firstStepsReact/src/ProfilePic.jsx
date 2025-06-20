function ProfilePicture(){
    const imageUrl = './scr/assets/wise-o-gato.jpg'
    const handleClick = () => console.log('ouch!')
    return(
        <img onClick={handleClick}> src="{imageUrl}" alt="" </img>
    )


}
export default ProfilePicture