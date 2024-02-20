import React,{memo,useState} from 'react'
import { preProcessFile } from 'typescript'

type FizzProps={
    isFizz:boolean
}

const Fizz=(props:FizzProps)=>{
    const {isFizz}= props
    console.log(`isFizz=${isFizz}`)
    return <span>
        {isFizz? 'Fizz':''}
    </span>
}

type BuzzProps={
    isBuzz:boolean
}

const Buzz=memo<BuzzProps>((props)=>{
    const {isBuzz}=props
    console.log('isBuzz=${isBuzz}')
    return (
        <span>
            {isBuzz?'Buzz':''}
        </span>
    )
})

export const Parent=()=>{
    const [count,setCount]=useState(1)
    const isFizz=count%3===0
    const isBuzz=count%5===0

    console.log((`Parent開始 count=${count}`))
    return(
        <div>
            <button onClick={()=>setCount((c)=>c+1)}>+1</button>
            <p>{`現在のカウント:${count}`}</p>
            <p>
                <Fizz isFizz={isFizz}/>
                <Buzz isBuzz={isBuzz}/>
            </p>
        </div>
    )
}