import {useState} from "react"
import { deflate } from "zlib"

type CounterProps={
    initialValue:number
}

const Counter=(props:CounterProps)=>{
    const {initialValue}=props

    const [count,setCount]=useState(initialValue)
    return(
        <div>
            <p>
                Count: {count}
            </p>
            <button onClick={()=>setCount(count-1)}>-</button>
            <button onClick={()=>setCount(count+1)}>+</button>
        </div>
    )
}

export default Counter