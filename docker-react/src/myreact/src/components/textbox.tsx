import React from 'react'

const Name=()=>{
    const onChange=(e:React.ChangeEvent<HTMLInputElement>)=>{
        console.log(e.target.value)
    }

    return(
        <div style={{padding: '16px',backgroundColor:'grey'}}>
        <label htmlFor='name'>
            <input id='name' className='input-name' type="text" onChange={onChange}>
            </input>        
        </label>
        </div>
    )
}

export default Name