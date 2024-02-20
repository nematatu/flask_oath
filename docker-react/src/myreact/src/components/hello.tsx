const Hello=()=>{
    const onClick=()=>{
        alert('hello, React!')
    }
    const text='hello'

    return (
        <div onClick={onClick}>
            {text}
        </div>
    )
}

export default Hello