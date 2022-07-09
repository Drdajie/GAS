# This file contains the evaluation functions

import re
import editdistance

sentiment_word_list = ['positive', 'negative', 'neutral']
aspect_cate_list = [
 'restaurant general',
 'restaurant prices',
 'restaurant miscellaneous',
 'food prices',
 'food quality',
 'food style_options',
 'drinks prices',
 'drinks quality',
 'drinks style_options',
 'ambience general',
 'service general',
 'location general'
 ]
 
acos_cate_list = [
 'RESTAURANT#GENERAL',
 'RESTAURANT#PRICES',
 'RESTAURANT#MISCELLANEOUS',
 'FOOD#PRICES',
 'FOOD#QUALITY',
 'FOOD#STYLE_OPTIONS',
 'DRINKS#PRICES',
 'DRINKS#QUALITY',
 'DRINKS#STYLE_OPTIONS',
 'AMBIENCE#GENERAL',
 'SERVICE#GENERAL',
 'LOCATION#GENERAL',
 'LAPTOP#GENERAL',
 'LAPTOP#PRICE',
 'LAPTOP#QUALITY',
 'LAPTOP#OPERATION_PERFORMANCE',
 'LAPTOP#USABILITY',
 'LAPTOP#DESIGN_FEATURES',
 'LAPTOP#PORTABILITY',
 'LAPTOP#CONNECTIVITY',
 'LAPTOP#MISCELLANEOUS',
 'DISPLAY#GENERAL',
 'DISPLAY#PRICE',
 'DISPLAY#QUALITY',
 'DISPLAY#OPERATION_PERFORMANCE',
 'DISPLAY#USABILITY',
 'DISPLAY#DESIGN_FEATURES',
 'DISPLAY#PORTABILITY',
 'DISPLAY#CONNECTIVITY',
 'DISPLAY#MISCELLANEOUS',
 'CPU#GENERAL',
 'CPU#PRICE',
 'CPU#QUALITY',
 'CPU#OPERATION_PERFORMANCE',
 'CPU#USABILITY',
 'CPU#DESIGN_FEATURES',
 'CPU#PORTABILITY',
 'CPU#CONNECTIVITY',
 'CPU#MISCELLANEOUS',
 'MOTHERBOARD#GENERAL',
 'MOTHERBOARD#PRICE',
 'MOTHERBOARD#QUALITY',
 'MOTHERBOARD#OPERATION_PERFORMANCE',
 'MOTHERBOARD#USABILITY',
 'MOTHERBOARD#DESIGN_FEATURES',
 'MOTHERBOARD#PORTABILITY',
 'MOTHERBOARD#CONNECTIVITY',
 'MOTHERBOARD#MISCELLANEOUS',
 'HARD_DISC#GENERAL',
 'HARD_DISC#PRICE',
 'HARD_DISC#QUALITY',
 'HARD_DISC#OPERATION_PERFORMANCE',
 'HARD_DISC#USABILITY',
 'HARD_DISC#DESIGN_FEATURES',
 'HARD_DISC#PORTABILITY',
 'HARD_DISC#CONNECTIVITY',
 'HARD_DISC#MISCELLANEOUS',
 'MEMORY#GENERAL',
 'MEMORY#PRICE',
 'MEMORY#QUALITY',
 'MEMORY#OPERATION_PERFORMANCE',
 'MEMORY#USABILITY',
 'MEMORY#DESIGN_FEATURES',
 'MEMORY#PORTABILITY',
 'MEMORY#CONNECTIVITY',
 'MEMORY#MISCELLANEOUS',
 'BATTERY#GENERAL',
 'BATTERY#PRICE',
 'BATTERY#QUALITY',
 'BATTERY#OPERATION_PERFORMANCE',
 'BATTERY#USABILITY',
 'BATTERY#DESIGN_FEATURES',
 'BATTERY#PORTABILITY',
 'BATTERY#CONNECTIVITY',
 'BATTERY#MISCELLANEOUS',
 'POWER_SUPPLY#GENERAL',
 'POWER_SUPPLY#PRICE',
 'POWER_SUPPLY#QUALITY',
 'POWER_SUPPLY#OPERATION_PERFORMANCE',
 'POWER_SUPPLY#USABILITY',
 'POWER_SUPPLY#DESIGN_FEATURES',
 'POWER_SUPPLY#PORTABILITY',
 'POWER_SUPPLY#CONNECTIVITY',
 'POWER_SUPPLY#MISCELLANEOUS',
 'KEYBOARD#GENERAL',
 'KEYBOARD#PRICE',
 'KEYBOARD#QUALITY',
 'KEYBOARD#OPERATION_PERFORMANCE',
 'KEYBOARD#USABILITY',
 'KEYBOARD#DESIGN_FEATURES',
 'KEYBOARD#PORTABILITY',
 'KEYBOARD#CONNECTIVITY',
 'KEYBOARD#MISCELLANEOUS',
 'MOUSE#GENERAL',
 'MOUSE#PRICE',
 'MOUSE#QUALITY',
 'MOUSE#OPERATION_PERFORMANCE',
 'MOUSE#USABILITY',
 'MOUSE#DESIGN_FEATURES',
 'MOUSE#PORTABILITY',
 'MOUSE#CONNECTIVITY',
 'MOUSE#MISCELLANEOUS',
 'FANS&COOLING#GENERAL',
 'FANS&COOLING#PRICE',
 'FANS&COOLING#QUALITY',
 'FANS&COOLING#OPERATION_PERFORMANCE',
 'FANS&COOLING#USABILITY',
 'FANS&COOLING#DESIGN_FEATURES',
 'FANS&COOLING#PORTABILITY',
 'FANS&COOLING#CONNECTIVITY',
 'FANS&COOLING#MISCELLANEOUS',
 'OPTICAL_DRIVES#GENERAL',
 'OPTICAL_DRIVES#PRICE',
 'OPTICAL_DRIVES#QUALITY',
 'OPTICAL_DRIVES#OPERATION_PERFORMANCE',
 'OPTICAL_DRIVES#USABILITY',
 'OPTICAL_DRIVES#DESIGN_FEATURES',
 'OPTICAL_DRIVES#PORTABILITY',
 'OPTICAL_DRIVES#CONNECTIVITY',
 'OPTICAL_DRIVES#MISCELLANEOUS',
 'PORTS#GENERAL',
 'PORTS#PRICE',
 'PORTS#QUALITY',
 'PORTS#OPERATION_PERFORMANCE',
 'PORTS#USABILITY',
 'PORTS#DESIGN_FEATURES',
 'PORTS#PORTABILITY',
 'PORTS#CONNECTIVITY',
 'PORTS#MISCELLANEOUS',
 'GRAPHICS#GENERAL',
 'GRAPHICS#PRICE',
 'GRAPHICS#QUALITY',
 'GRAPHICS#OPERATION_PERFORMANCE',
 'GRAPHICS#USABILITY',
 'GRAPHICS#DESIGN_FEATURES',
 'GRAPHICS#PORTABILITY',
 'GRAPHICS#CONNECTIVITY',
 'GRAPHICS#MISCELLANEOUS',
 'MULTIMEDIA_DEVICES#GENERAL',
 'MULTIMEDIA_DEVICES#PRICE',
 'MULTIMEDIA_DEVICES#QUALITY',
 'MULTIMEDIA_DEVICES#OPERATION_PERFORMANCE',
 'MULTIMEDIA_DEVICES#USABILITY',
 'MULTIMEDIA_DEVICES#DESIGN_FEATURES',
 'MULTIMEDIA_DEVICES#PORTABILITY',
 'MULTIMEDIA_DEVICES#CONNECTIVITY',
 'MULTIMEDIA_DEVICES#MISCELLANEOUS',
 'HARDWARE#GENERAL',
 'HARDWARE#PRICE',
 'HARDWARE#QUALITY',
 'HARDWARE#OPERATION_PERFORMANCE',
 'HARDWARE#USABILITY',
 'HARDWARE#DESIGN_FEATURES',
 'HARDWARE#PORTABILITY',
 'HARDWARE#CONNECTIVITY',
 'HARDWARE#MISCELLANEOUS',
 'OS#GENERAL',
 'OS#PRICE',
 'OS#QUALITY',
 'OS#OPERATION_PERFORMANCE',
 'OS#USABILITY',
 'OS#DESIGN_FEATURES',
 'OS#PORTABILITY',
 'OS#CONNECTIVITY',
 'OS#MISCELLANEOUS',
 'SOFTWARE#GENERAL',
 'SOFTWARE#PRICE',
 'SOFTWARE#QUALITY',
 'SOFTWARE#OPERATION_PERFORMANCE',
 'SOFTWARE#USABILITY',
 'SOFTWARE#DESIGN_FEATURES',
 'SOFTWARE#PORTABILITY',
 'SOFTWARE#CONNECTIVITY',
 'SOFTWARE#MISCELLANEOUS',
 'WARRANTY#GENERAL',
 'WARRANTY#PRICE',
 'WARRANTY#QUALITY',
 'WARRANTY#OPERATION_PERFORMANCE',
 'WARRANTY#USABILITY',
 'WARRANTY#DESIGN_FEATURES',
 'WARRANTY#PORTABILITY',
 'WARRANTY#CONNECTIVITY',
 'WARRANTY#MISCELLANEOUS',
 'SHIPPING#GENERAL',
 'SHIPPING#PRICE',
 'SHIPPING#QUALITY',
 'SHIPPING#OPERATION_PERFORMANCE',
 'SHIPPING#USABILITY',
 'SHIPPING#DESIGN_FEATURES',
 'SHIPPING#PORTABILITY',
 'SHIPPING#CONNECTIVITY',
 'SHIPPING#MISCELLANEOUS',
 'SUPPORT#GENERAL',
 'SUPPORT#PRICE',
 'SUPPORT#QUALITY',
 'SUPPORT#OPERATION_PERFORMANCE',
 'SUPPORT#USABILITY',
 'SUPPORT#DESIGN_FEATURES',
 'SUPPORT#PORTABILITY',
 'SUPPORT#CONNECTIVITY',
 'SUPPORT#MISCELLANEOUS',
 'COMPANY#GENERAL',
 'COMPANY#PRICE',
 'COMPANY#QUALITY',
 'COMPANY#OPERATION_PERFORMANCE',
 'COMPANY#USABILITY',
 'COMPANY#DESIGN_FEATURES',
 'COMPANY#PORTABILITY',
 'COMPANY#CONNECTIVITY',
 'COMPANY#MISCELLANEOUS'
 ]


def extract_spans_extraction(task, seq):
    extractions = []
    if task == 'uabsa' and seq.lower() == 'none':
        return []
    else:
        if task in ['uabsa', 'aope']:
            all_pt = seq.split('; ')
            for pt in all_pt:
                pt = pt[1:-1]
                try:
                    a, b = pt.split(', ')
                except ValueError:
                    a, b = '', ''
                extractions.append((a, b))
        elif task in ['tasd', 'aste']:
            all_pt = seq.split('; ')
            for pt in all_pt:
                pt = pt[1:-1]
                try:
                    a, b, c = pt.split(', ')
                except ValueError:
                    a, b, c = '', '', ''
                extractions.append((a, b, c))            
        return extractions


def extract_spans_annotation(task, seq):
    if task in ['aste', 'tasd']:
        extracted_spans = extract_triplets(seq)
    elif task in ['aope', 'uabsa']:
        extracted_spans = extract_pairs(seq)
    elif task == "acos":
        extracted_spans = extract_quadruples(seq)
    elif 'acos' in task:
        extracted_spans = extract_quadruples(seq)

    return extracted_spans


def extract_pairs(seq):
    aps = re.findall('\[.*?\]', seq)
    aps = [ap[1:-1] for ap in aps]          # 只要 [] 中的内容 -> 可以两步合并为 findall('\[(.*?)\]', seq)
    pairs = []
    for ap in aps:
        # the original sentence might have 
        try:
            at, ots = ap.split('|')
        except ValueError:
            at, ots  = '', ''
        
        if ',' in ots:     # multiple ots 
            for ot in ots.split(', '):
                pairs.append((at, ot))
        else:
            pairs.append((at, ots))    
    return pairs        


def extract_triplets(seq):
    aps = re.findall('\[.*?\]', seq)
    aps = [ap[1:-1] for ap in aps]
    triplets = []
    for ap in aps:
        try:
            a, b, c = ap.split('|')
        except ValueError:
            a, b, c = '', '', ''
        
        # for ASTE
        if b in sentiment_word_list:
            if ',' in c:
                for op in c.split(', '):
                    triplets.append((a, b, op))
            else:
                triplets.append((a, b, c))
        # for TASD
        else:
            if ',' in b:
                for ac in b.split(', '):
                    triplets.append((a, ac, c))
            else:
                triplets.append((a, b, c))

    return triplets

def extract_quadruples(seq):
    sentiments = ['positive', 'negative', 'neutral', 'conflict']
    aps = re.findall('\[.*?\]', seq)
    aps = [ap[1:-1] for ap in aps]
    quadruples = []
    for ap in aps:
        acs = ap.split("; ")     # 一个 aspect term 对应的所有 aspect category
        at = ''
        for i, temp in enumerate(acs):
            if i == 0:
                try:
                    at, ac, ops, st = temp.split('|')          # "at|ac|op|st"
                except ValueError:
                    at, ac, ops, st = '', '', '', ''
            else:
                try:
                    ac, ops, st = temp.split('|')          # "ac|op|st"
                except ValueError:
                    ac, ops, st = '', '', ''

            if ',' in ops:     # multiple ops 
                for op in ops.split(', '):
                    quadruples.append((at, ac, op, st))
            else:
                quadruples.append((at, ac, ops, st))

    return quadruples

def recover_terms_with_editdistance(original_term, sent):
    words = original_term.split(' ')
    new_words = []
    for word in words:
        edit_dis = []
        for token in sent:
            edit_dis.append(editdistance.eval(word, token))
        smallest_idx = edit_dis.index(min(edit_dis))
        new_words.append(sent[smallest_idx])
    new_term = ' '.join(new_words)
    return new_term


def fix_preds_uabsa(all_pairs, sents):
    all_new_pairs = []
    for i, pairs in enumerate(all_pairs):
        new_pairs = []
        if pairs == []:
            all_new_pairs.append(pairs)
        else:
            for pair in pairs:
                # AT not in the original sentence
                if pair[0] not in  ' '.join(sents[i]):
                    # print('Issue')
                    new_at = recover_terms_with_editdistance(pair[0], sents[i])
                else:
                    new_at = pair[0]

                if pair[1] not in sentiment_word_list:
                    new_sentiment = recover_terms_with_editdistance(pair[1], sentiment_word_list)
                else:
                    new_sentiment = pair[1]

                new_pairs.append((new_at, new_sentiment))
                # print(pair, '>>>>>', word_and_sentiment)
                # print(all_target_pairs[i])
            all_new_pairs.append(new_pairs)

    return all_new_pairs


def fix_preds_aope(all_pairs, sents):

    all_new_pairs = []

    for i, pairs in enumerate(all_pairs):
        new_pairs = []
        if pairs == []:
            all_new_pairs.append(pairs)
        else:
            for pair in pairs:
                #print(pair)
                # AT not in the original sentence
                if pair[0] not in  ' '.join(sents[i]):
                    # print('Issue')
                    new_at = recover_terms_with_editdistance(pair[0], sents[i])
                else:
                    new_at = pair[0]

                # OT not in the original sentence
                ots = pair[1].split(', ')
                new_ot_list = []
                for ot in ots:
                    if ot not in ' '.join(sents[i]):
                        # print('Issue')
                        new_ot_list.append(recover_terms_with_editdistance(ot, sents[i]))
                    else:
                        new_ot_list.append(ot)
                new_ot = ', '.join(new_ot_list)

                new_pairs.append((new_at, new_ot))
                # print(pair, '>>>>>', word_and_sentiment)
                # print(all_target_pairs[i])
            all_new_pairs.append(new_pairs)

    return all_new_pairs


# for ASTE
def fix_preds_aste(all_pairs, sents):

    all_new_pairs = []

    for i, pairs in enumerate(all_pairs):
        new_pairs = []
        if pairs == []:
            all_new_pairs.append(pairs)
        else:
            for pair in pairs:
                #two formats have different orders
                p0, p1, p2 = pair
                # for annotation-type
                if p1 in sentiment_word_list:
                    at, ott, ac = p0, p2, p1
                    io_format = 'annotation'
                # for extraction type
                elif p2 in sentiment_word_list:
                    at, ott, ac = p0, p1, p2
                    io_format = 'extraction'

                #print(pair)
                # AT not in the original sentence
                if at not in  ' '.join(sents[i]):
                    # print('Issue')
                    new_at = recover_terms_with_editdistance(at, sents[i])
                else:
                    new_at = at
                
                if ac not in sentiment_word_list:
                    new_sentiment = recover_terms_with_editdistance(ac, sentiment_word_list)
                else:
                    new_sentiment = ac
                
                # OT not in the original sentence
                ots = ott.split(', ')
                new_ot_list = []
                for ot in ots:
                    if ot not in ' '.join(sents[i]):
                        # print('Issue')
                        new_ot_list.append(recover_terms_with_editdistance(ot, sents[i]))
                    else:
                        new_ot_list.append(ot)
                new_ot = ', '.join(new_ot_list)
                if io_format == 'extraction':
                    new_pairs.append((new_at, new_ot, new_sentiment))
                else:
                    new_pairs.append((new_at, new_sentiment, new_ot))
                # print(pair, '>>>>>', word_and_sentiment)
                # print(all_target_pairs[i])
            all_new_pairs.append(new_pairs)
    
    return all_new_pairs


def fix_preds_tasd(all_pairs, sents):

    all_new_pairs = []

    for i, pairs in enumerate(all_pairs):
        new_pairs = []
        if pairs == []:
            all_new_pairs.append(pairs)
        else:
            for pair in pairs:
                #print(pair)
                # AT not in the original sentence
                sents_and_null = ' '.join(sents[i]) + 'NULL'
                if pair[0] not in  sents_and_null:
                    # print('Issue')
                    new_at = recover_terms_with_editdistance(pair[0], sents[i])
                else:
                    new_at = pair[0]
                
                # AC not in the list
                acs = pair[1].split(', ')
                new_ac_list = []
                for ac in acs:
                    if ac not in aspect_cate_list:
                        new_ac_list.append(recover_terms_with_editdistance(ac, aspect_cate_list))
                    else:
                        new_ac_list.append(ac)
                new_ac = ', '.join(new_ac_list)
                
                if pair[2] not in sentiment_word_list:
                    new_sentiment = recover_terms_with_editdistance(pair[2], sentiment_word_list)
                else:
                    new_sentiment = pair[2]
            
                new_pairs.append((new_at, new_ac, new_sentiment))
                # print(pair, '>>>>>', word_and_sentiment)
                # print(all_target_pairs[i])
            all_new_pairs.append(new_pairs)
    
    return all_new_pairs

def fix_preds_acos(all_pairs, sents):
    all_new_pairs = []
    for i, pairs in enumerate(all_pairs):
        new_pairs = []
        if pairs == []:
            all_new_pairs.append(pairs)
        else:
            for pair in pairs:
                #print(pair)
                # AT not in the original sentence
                sents_and_null = ' '.join(sents[i]) + 'NULL'
                if pair[0] not in  sents_and_null:
                    # print('Issue')
                    new_at = recover_terms_with_editdistance(pair[0], sents[i])
                else:
                    new_at = pair[0]
                
                # AC not in the list
                if pair[1] not in acos_cate_list:
                    new_ac = recover_terms_with_editdistance(pair[1], acos_cate_list)
                else:
                    new_ac = pair[1]
                
                # OT not in the original sentence
                ots = pair[2].split(', ')
                new_ot_list = []
                for ot in ots:
                    if ot not in sents_and_null:
                        # print('Issue')
                        new_ot_list.append(recover_terms_with_editdistance(ot, sents[i]))
                    else:
                        new_ot_list.append(ot)
                new_ot = ', '.join(new_ot_list)
                
                
                if pair[3] not in sentiment_word_list:
                    new_sentiment = recover_terms_with_editdistance(pair[2], sentiment_word_list)
                else:
                    new_sentiment = pair[3]
            
                new_pairs.append((new_at, new_ac, new_ot, new_sentiment))
                # print(pair, '>>>>>', word_and_sentiment)
                # print(all_target_pairs[i])
            all_new_pairs.append(new_pairs)
    
    return all_new_pairs

def fix_pred_with_editdistance(all_predictions, sents, task):
    if task == 'uabsa':
        fixed_preds = fix_preds_uabsa(all_predictions, sents)
    elif task == 'aope':
        fixed_preds = fix_preds_aope(all_predictions, sents) 
    elif task == 'aste': 
        fixed_preds = fix_preds_aste(all_predictions, sents) 
    elif task == 'tasd':
        fixed_preds = fix_preds_tasd(all_predictions, sents) 
    elif task == 'acos':
        fixed_preds = fix_preds_acos(all_predictions, sents)
    elif 'acos' in task:
        fixed_preds = fix_preds_acos(all_predictions, sents)
    else:
        print("*** Unimplemented Error ***")
        fixed_preds = all_predictions

    return fixed_preds


def compute_f1_scores(pred_pt, gold_pt):
    """
    Function to compute F1 scores with pred and gold pairs/triplets
    The input needs to be already processed
    """
    # number of true postive, gold standard, predicted aspect terms
    n_tp, n_gold, n_pred = 0, 0, 0

    for i in range(len(pred_pt)):
        n_gold += len(gold_pt[i])
        n_pred += len(pred_pt[i])

        for t in pred_pt[i]:
            if t in gold_pt[i]:
                n_tp += 1

    precision = float(n_tp) / float(n_pred) if n_pred != 0 else 0
    recall = float(n_tp) / float(n_gold) if n_gold != 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if precision != 0 or recall != 0 else 0
    scores = {'precision': precision, 'recall': recall, 'f1': f1}

    return scores


def print_fault_instance(pred_seqs, gold_seqs, num_samples):
    """
    输出一些错误实例。
    """
    num = 0
    for i in range(num_samples):
        if pred_seqs[i] != gold_seqs[i]:
            num += 1
            print("goal：" + gold_seqs[i])
            print("pred：" + pred_seqs[i])
            print()
    print('-------------------------------------------')
    print(num)


def compute_scores(pred_seqs, gold_seqs, sents, io_format, task, flag = False):
    """
    compute metrics for multiple tasks
    """
    assert len(pred_seqs) == len(gold_seqs) 
    num_samples = len(gold_seqs)

    # if flag:
    #     print_fault_instance(pred_seqs, gold_seqs, num_samples)

    all_labels, all_predictions = [], []                # [[],[],[],...]

    for i in range(num_samples):
        if io_format == 'annotation':
            gold_list = extract_spans_annotation(task, gold_seqs[i])
            pred_list = extract_spans_annotation(task, pred_seqs[i])
        elif io_format == 'extraction':
            gold_list = extract_spans_extraction(task, gold_seqs[i])
            pred_list = extract_spans_extraction(task, pred_seqs[i])

        all_labels.append(gold_list)
        all_predictions.append(pred_list)
    
    print("\nResults of raw output")
    raw_scores = compute_f1_scores(all_predictions, all_labels)
    print(raw_scores)

    # fix the issues due to generation
    all_predictions_fixed = fix_pred_with_editdistance(all_predictions, sents, task)
    print("\nResults of fixed output")
    fixed_scores = compute_f1_scores(all_predictions_fixed, all_labels)
    print(fixed_scores)
    
    return raw_scores, fixed_scores, all_labels, all_predictions, all_predictions_fixed