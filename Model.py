
from huggingface_hub  import InferenceClient
from apikey  import hugging_face_key

class  Model:
    
    def __init__(self,
                model_name, 
                temperature, 
                top_p, 
                endpoint_url,
                top_k,
                repetition_penalty,
                stop_sequence) :
        
        self.model_name =  model_name,
        self.temperature = temperature,
        self.top_p = top_p,
        self.endpoint_url = endpoint_url,
        self.top_k = top_k,
        self.repetition_penalty = repetition_penalty,
        self.stop_sequence = stop_sequence

    def Query(self, prompt):
        ##  endpoint
        ## hub key
        #client
        client = InferenceClient(self.endpoint_url , token=hugging_face_key) 
        response = client.text_generation(prompt, details = True)
        return response




        
