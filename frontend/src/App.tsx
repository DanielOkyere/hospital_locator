import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
<<<<<<< HEAD
import Map from './map'
import Navbar from './navbar'
import SearchForm from './searchform'

function App() {
  const [count, setCount] = useState(0)
  const username = 'Daniel';
  return (
    <div className="App">
      <Navbar username={username} />
      <h1 className="text-3xl font-bold underline">
        Welcome To The Hospital Locator
      </h1>
      <SearchForm onSearch={(query) => console.log(`Searching for: ${query}`)} />
      <Map />
      <Map />
=======

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
>>>>>>> 31c155a (Setup)
    </div>
  )
}

export default App
