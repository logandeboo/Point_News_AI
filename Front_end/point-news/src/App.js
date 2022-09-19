
import Navbar from './components/Navbar'
import './App.css'
import ItemFeed from './components/ItemFeed'



function App() {
  let topicPath

  switch (window.location.pathname){
    
    case "/Politics":
      topicPath = '/Politics'
      break
    case "/Business":
      topicPath = '/Business'
      break
    case "/Technology":
      topicPath = '/Technology'
      break
    case "/Science":
      topicPath = '/Science'
      break
    case "/Entertainment":
      topicPath = '/Entertainment'
      break    
    case "/Health":
      topicPath = '/Health'
      break
    case "/Environment":
      topicPath = '/Environment'
      break
    default:
      topicPath='/Politics'
    
  }
  return (
    <div>
      <Navbar/>
      <ItemFeed topic={topicPath}/>
    </div>
    
  )
}

export default App  