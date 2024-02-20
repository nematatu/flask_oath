import exp from "constants"
import React from "react"

//物流倉庫
const TitleContext=React.createContext('')

//物流倉庫から値を取り出して何かを返す､いわば加工者
const Title=()=>{
    return(
        <TitleContext.Consumer>
            {(title)=>{
                return <h1>{title}</h1>
            }}
        </TitleContext.Consumer>
    )
}

const Page=()=>{
    return(
        //値を与えるだけのもの
        <TitleContext.Provider value={"title"}>
            <Title/>
        </TitleContext.Provider>
    )
}
export default Page