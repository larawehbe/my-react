import logo from './logo.svg';
import './App.css';
import React from 'react';
import SparklesForm from './components/myform';

function App() {
  return (
    <div >
       <nav class="navbar navbar-light bg-light ">
          <span class="navbar-brand mb-0  h1">Sparkles.AI</span>
        </nav>
      <SparklesForm />
     
    </div>
  );
}

export default App;
