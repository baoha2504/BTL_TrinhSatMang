import torch
from transformers import RobertaForSequenceClassification, AutoTokenizer


def detect_sentiment(sentence):
    try:
        if sentence != None:
            model = RobertaForSequenceClassification.from_pretrained("../textprocessing/wonrax/phobert-base-vietnamese-sentiment")

            tokenizer = AutoTokenizer.from_pretrained("../textprocessing/wonrax/phobert-base-vietnamese-sentiment", use_fast=False)

            input_ids = torch.tensor([tokenizer.encode(sentence)])

            with torch.no_grad():
                out = model(input_ids)
                results = out.logits.softmax(dim=-1).tolist()
                # Tìm giá trị lớn nhất và chỉ số của nó
                max_value = max(results[0])
                max_index = results[0].index(max_value)
                
                if(max_index == 0):
                    return "Tiêu cực"
                elif(max_index == 1):
                    return "Tích cực"
                else:
                    return "Trung lập"
        else:
            return "Không xác định"
                
    except Exception as e:
        print("Lỗi: ", str(e))
    # Output:
    # [[0.002, 0.988, 0.01]]
    #     ^      ^      ^
    #    NEG    POS    NEU   
    
    
# NEG: Tiêu cực
# POS: Tích cực
# NEU: Trung lập