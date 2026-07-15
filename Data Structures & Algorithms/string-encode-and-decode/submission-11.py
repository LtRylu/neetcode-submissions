class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return "0"
        if not strs:
            return ""
        array_length = len(strs)
        encode_array = []
        i = 0
        while i < array_length:
            string = strs[i]
            len_str = len(string)
            len_jump = len(str(len_str))
            encode_array.append(f"{len_jump}{len_str}{string}")
            i += 1
        return "".join(encode_array)
            

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == "0":
            return [""]
        len_str = len(s)
        decoded_array = []
        i = 0
        current_index = 0
        while i < len_str:
            current_string_array = []
            if int(s[current_index]) == 1:
                jump = int(s[current_index + 1])
                current_index += 1
            elif int(s[current_index]) == 2: 
                jump = int(s[current_index + 1] + s[current_index + 2])
                current_index += 2
            elif int(s[current_index]) == 3:
                jump = int(s[current_index + 1] + s[current_index + 2] + s[current_index + 3])
                current_index += 3
            i = current_index + 1
            current_index = current_index + jump + 1
            while i < current_index:
                current_string_array.append(s[i])
                i += 1
            current_string = "".join(current_string_array)
            decoded_array.append(current_string)
        return decoded_array
        
            
            
