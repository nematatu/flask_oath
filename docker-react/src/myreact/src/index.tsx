import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Hello from './components/hello';
import Name from './components/textbox';
import Message from './components/message';
import Container from './components/ContainerSample'
import Page from './components/ContextSample'
import reportWebVitals from './reportWebVitals';
import Counter from './components/ClickCounter'
import Counter2 from './components/ClickCounterReducer'
import {Parent} from './components/parent'
import { CONNREFUSED } from 'dns';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <Hello />
    <Name />
    <Message/>
    <Container/>
    <Page/>
    <Counter initialValue={0}/>
    <Counter2 initialValue={0}/>
    <Parent/> 
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
