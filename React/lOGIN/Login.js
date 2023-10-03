import "../Styles/Login.css"

import React, { useEffect, useState } from 'react'

import Home from './Home'
import { Link } from 'react-router-dom'
import axios from 'axios'
import bg from "../Assests/bg.jpg"
import logo from "../Assests/logo.jpg"
import { useNavigate } from 'react-router-dom'

function Login() {
  let page=useNavigate();
  const [username,setUsername]=useState("")
  const [password,setPassword]=useState("")

  const[APIData,setAPIData] = useState([])

  useEffect(() => {
    axios.get(`http://localhost:3004/data`)
        .then((response) => {
            setAPIData(response.data);         
        })  
}, [])
 
// useEffect(()=>{
//   axios.get()
// },[])
  const submitHAndler=(e)=>{
    e.preventDefault();
    {APIData.map((data)=>{
      if(data.userName==username && data.password==password){
        // console.log(data.userName)
        page('/Product')
        localStorage.setItem("username",username)
        localStorage.setItem("password",password)
        // console.log(APIData)
      }
      else{
        console.log(null)
      }
    })}
  }
  return (
    <div className='container-fluid bg'>
      <div className='row'>
        <div className='col-4'>

        </div>
        <div className='col-4'>
          <div className='box'>
            <form  className="form">
              <h1>Login Form</h1>
              <img src={logo}/>
              <div className='form-group'>
                <label>Username</label>
                <input className='form-control' type="text" placeholder='Enter Username' 
                value={username} onChange={(e)=>setUsername(e.target.value)}/>
              </div>
              <div className='form-group'>
                <label>Password</label>
                <input className='form-control ' type="password" placeholder='Enter password' 
                value={password} onChange={(e)=>setPassword(e.target.value)}/>
              </div>
           <button className='btn btn-primary form-control' type='submit'onClick={submitHAndler}>Submit</button>
            </form>
          </div>
        </div>
        <div className='col-4'>

        </div>
      </div>
    </div>
  )
}

export default Login