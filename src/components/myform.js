import React from 'react';
import axios from 'axios';
import  ReactDOM  from 'react';

class SparklesForm extends React.Component {
    constructor(props){
        super(props)    
        this.state = {  content_type: '', detauseStateils: '', person_pov: '', tones: '', result: ''}
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
      }

    
      
      // Form submitting logic, prevent default page refresh 
       handleSubmit(event){
        const { content_type, details, person_pov, tones } = this.state
        event.preventDefault()
        console.log(this.state)
        let url = 'http://3.216.124.192:8000/sparkles/'
    let data = {
        "content_type": "Freestyle",
        "details": "Connect django with react",
        "person_pov": "First person",
        "tone": "[Friendly,Professional]",
    }
    let form_data = {
      'content_type' : content_type,
      'details' : details,
      'person_pov' : person_pov,
      'tone' : tones
    }
    axios.post(url, form_data).then(response => {
        console.log(response.data);
        this.setState({result: response.data})
        // return response.data;
    }).catch(error => {
        console.log(error);
        return error;
    });
  }
      
     
      handleChange(event){
        this.setState({
          // Computed property names
          // keys of the objects are computed dynamically
          [event.target.name] : event.target.value
        })
      }
      

      render(){
        return(
          <>
                    <form onSubmit={this.handleSubmit}>
            
            
            
            <div>
                <label htmlFor='content_type'>What are you looking to create?</label>
                <input
                name='content_type'
                placeholder='Content Type'
                value={this.state.content_type}
                onChange={this.handleChange}
                />
            </div>


            <div>
            <label  htmlFor='details'>what are the main points you want to cover?</label>
            <input 
            name='details'
            placeholder= 'Details'
            value={this.state.details}
            onChange={this.handleChange}
            />
            
            </div>
            <div>
            <label  htmlFor='person_pov'>what are the main points you want to cover?</label>
            <input 
            name='person_pov'
            placeholder= 'Speak as: I,we or You,we or He,She,It'
            value={this.state.person_pov}
            onChange={this.handleChange}
            />
            
            </div>
            <div>
            <label  htmlFor='tones'>what are the main points you want to cover?</label>
            <input 
            name='tones'
            placeholder= 'Tones:'
            value={this.state.tones}
            onChange={this.handleChange}
            />
            
            </div>

            <div>
              <button>Create Account</button>
            </div>
          </form>
          {this.state.result !== ""?
          <div><h6>result now from gpt3: </h6><h6>{JSON.stringify(this.state.result.result['result'])}</h6></div>
        :
        null
        }</>
        )
      }
  }
  

export default SparklesForm;