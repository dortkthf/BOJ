def solution(new_id):
    answer = ''
    new_id = new_id.lower() 
    
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-','_','.']:
            continue
        else:
            new_id = new_id.replace(i,'')
    
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:] if len(new_id) > 1 else ''
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1] if len(new_id) > 1 else ''
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id
