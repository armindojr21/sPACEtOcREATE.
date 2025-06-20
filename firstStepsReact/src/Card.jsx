import wiseOgato from './assets/wise-o-gato.jpg'
function Card(){
    return(
        <div className="card">
            <img className='image' src={wiseOgato} alt="me and my cat shirtless" />
            <h1 className='title'> Armindo Jr.</h1>
            <p className='message'>I am a <strong>musician</strong> and an aspirant <strong>computer science engineer</strong>.</p>
        </div>
    )
}export default Card