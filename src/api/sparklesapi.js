import axios from "axios";

function createContent() {
    let url = 'http://localhost:8000/sparkles/'
    let data = {
        "content_type": "Freestyle",
        "details": "Connect django with react",
        "person_pov": "First person",
        "tone": "[Friendly,Professional]",
    }
    
    axios.post(url, data).then(response => {
        console.log(response.data);
        return response.data;
    }).catch(error => {
        console.log(error);
        return error;
    });
}

export default createContent;