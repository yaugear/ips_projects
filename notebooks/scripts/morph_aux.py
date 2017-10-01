#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

MORPHEMES = [u'1PL(\u0431\u042b\u0437)', u'1PL(\u043a)', u'1SG(\u043c)', u'1SG(\u043c\u042b\u043d)', u'2PL(\u0433\u042b\u0437)', u'2PL(\u0441\u042b\u0437)', u'2SG(\u0441\u042b\u04a3)', u'2SG(\u04a3)', u'3PL(\u041b\u0410\u0440)', u'3SG(\u0414\u042b\u0440)', u'ABL(\u0414\u0410\u043d)', u'ACC(\u043d\u042b)', u'ADVV_ACC(\u042b\u043f)', u'ADVV_ANT(\u0413\u0410\u0447)', u'ADVV_NEG(\u0419\u0447\u0410)', u'ADVV_SUCC(\u0413\u0410\u043d\u0447\u042b)', u'AFC(\u043a\u0410\u0439)', u'ATTR_ABES(\u0441\u042b\u0437)', u'ATTR_GEN(\u043d\u042b\u043a\u042b)', u'ATTR_LOC(\u0414\u0410\u0433\u042b)', u'ATTR_MUN(\u043b\u042b)', u'Adj', u'Adv', u'CAUS(\u0414\u042b\u0440)', u'CAUS(\u0442)', u'CNJ', u'COMP(\u0440\u0410\u043a)', u'COND(\u0441\u0410)', u'DESID(\u043c\u0410\u043a\u0447\u042b)', u'DIM(\u0447\u042b\u043a)', u'DIR(\u0413\u0410)', u'DIR_LIM(\u0413\u0410\u0447\u0410)', u'DISTR(\u043b\u0410\u043f)', u'EQU(\u0447\u0410)', u'FUT_DEF(\u0410\u0447\u0410\u043a)', u'FUT_INDF(\u042b\u0440)', u'FUT_INDF_NEG(\u043c\u0410\u0441)', u'GEN(\u043d\u042b\u04a3)', u'HOR_PL(\u0419\u043a)', u'HOR_SG(\u0419\u043c)', u'IMP_PL(\u042b\u0433\u042b\u0437)', u'IMP_SG()', u'INF_1(\u042b\u0440\u0433\u0410)', u'INF_1(\u0441\u043a\u0410)', u'INF_2(\u043c\u0410\u043a)', u'INT(\u043c\u042b)', u'INTRJ', u'INT_MIR(\u043c\u042b\u043d\u0438)', u'JUS_PL(\u0441\u042b\u043d\u043d\u0410\u0440)', u'JUS_SG(\u0441\u042b\u043d)', u'LOC(\u0414\u0410)', u'Latin', u'Letter', u'MOD', u'MSRE(\u043b\u0410\u0442\u0410)', u'N', u'NEG(\u043c\u0410)', u'NMLZ(\u043b\u042b\u043a)', u'NUM_APPR(\u043b\u0410\u043f)', u'NUM_COLL(\u0410\u0423)', u'NUM_DISR(\u0448\u0410\u0440)', u'NUM_ORD(\u042b\u043d\u0447\u042b)', u'Nom', u'Num', u'OBL(\u0419\u0441\u042b)', u'PART', u'PASS(\u042b\u043b)', u'PCP_FUT(\u0410\u0447\u0410\u043a)', u'PCP_FUT(\u042b\u0440)', u'PCP_FUT(\u043c\u0410\u0441)', u'PCP_PR(\u0447\u042b)', u'PCP_PS(\u0413\u0410\u043d)', u'PL(\u041b\u0410\u0440)', u'PN', u'POSS_1PL(\u042b\u0431\u042b\u0437)', u'POSS_1SG(\u042b\u043c)', u'POSS_2PL(\u042b\u0433\u042b\u0437)', u'POSS_2SG(\u042b\u04a3)', u'POSS_3(\u0421\u042b)', u'POST', u'PREC_1(\u0447\u042b)', u'PREM(\u043c\u0410\u0433\u0410\u0439)', u'PRES(\u0419)', u'PROB(\u0414\u042b\u0440)', u'PROF(\u0447\u042b)', u'PROP', u'PSBL(\u043b\u042b\u043a)', u'PST_DEF(\u0414\u042b)', u'PST_INDF(\u0413\u0410\u043d)', u'RAR_1(\u0413\u0410\u043b\u0410)', u'RAR_2(\u042b\u0448\u0442\u042b\u0440)', u'RECP(\u042b\u0448)', u'REFL(\u042b\u043d)', u'Rus', u'SIM_1(\u0414\u0410\u0439)', u'SIM_2(\u0441\u044b\u043c\u0430\u043d)', u'Sg', u'Sign', u'Type1', u'Type2', u'Type3', u'Type4', u'USIT(\u0447\u0410\u043d)', u'V', u'VN_1(\u0443/\u04af/\u0432)', u'VN_2(\u042b\u0448)']

def chain2bin(morph, t=int):
    result = [t(0)] * len(MORPHEMES)

    for morpheme in morph.strip(';').replace(';', '+').split('+'):
        if morpheme in MORPHEMES:
            result[MORPHEMES.index(morpheme)] = t(1)

    return result


def diff(a, b):
    if len(a) != len(b):
        raise Exception('Length must be the same')
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1

    return diff


def diffd(a, b):
    if len(a) != len(b):
        raise Exception('Length must be the same')
    diff = 0
    for i in range(len(a)):
        diff += (a[i] - b[i]) * (a[i] - b[i])

    return math.sqrt(diff)


def testit(data, model):
    err = 0
    for (x, y) in data:
        if tuple(y) != tuple(model.predict([x])[0]):
            err += 1
    return err, len(data)


def testit_with_h(data, model, h):
    err = 0
    for (x, y) in data:
        if diff(y, model.predict([x])[0]) >= h:
            err += 1
    return err, len(data)


def testit_with_hd(data, model, h):
    err = 0
    for (x, y) in data:
        if diffd(y, model.predict_proba([x])[0]) >= h:
            err += 1
    return err, len(data)


def testit_val(data, model):
    err = 0
    for (x, y) in data:
        pred = model.predict([x])[0]
        ambiguity = y[0]
        correct = y[1]
        max_diff = 106
        max_chain = None
        for chain in ambiguity.strip(';').split(';'):
            bin_chain = chain2bin(chain)
            cdiff = diff(bin_chain, pred)
            if cdiff < max_diff:
                max_diff = cdiff
                max_chain = bin_chain
        if max_chain != correct:
            err += 1
    return err, len(data)


def testit_val_with_h(data, model, h):
    err = 0
    processed = len(data)
    for (x, y) in data:
        pred = model.predict([x])[0]
        ambiguity = y[0]
        correct = y[1]
        # coverage
        if diff(pred, correct) >= h:
            processed -= 1
            continue
        max_diff = 106
        max_chain = None
        for chain in ambiguity.strip(';').split(';'):
            bin_chain = chain2bin(chain)
            cdiff = diff(bin_chain, pred)
            if cdiff < max_diff:
                max_diff = cdiff
                max_chain = bin_chain
        if max_chain != correct:
            err += 1
    return err, len(data), processed


def testit_val_with_hd(data, model, h):
    err = 0
    processed = len(data)
    for (x, y) in data:
        pred = model.predict_proba([x])[0]
        ambiguity = y[0]
        correct = y[1]
        # coverage
        if diffd(pred, correct) >= h:
            processed -= 1
            continue
        max_diff = 106
        max_chain = None
        for chain in ambiguity.strip(';').split(';'):
            bin_chain = chain2bin(chain)
            cdiff = diffd(bin_chain, pred)
            if cdiff < max_diff:
                max_diff = cdiff
                max_chain = bin_chain
        if max_chain != correct:
            err += 1
    return err, len(data), processed


def acc_cover(data, model):
    resA = []
    resC = []
    for i in range(1, 10):
        err, lenX, lenA = testit_val_with_h(data, model, i)
        if lenA > 0:
            resA.append((lenA - err) * 100./lenA)
            resC.append(lenA * 100./lenX)

    return resA, resC


def load_validation_data(VERIFIED_TEXT_DISAMED_FILE, VERIFIED_TEXT_WORDS_FILE):
    with open(VERIFIED_TEXT_DISAMED_FILE, 'rb') as stream:
        data = stream.read().decode('utf-8')

    disamed = {}
    for line in data.split('\n'):
        if not line:
            continue
        wid, uid, dt, disamed_morph = line.split('\t')
        disamed[wid] = disamed_morph

    with open(VERIFIED_TEXT_WORDS_FILE, 'rb') as stream:
        data = stream.read().decode('utf-8')

    empty = [0] * 106
    result = []
    sentence = []
    res = []

    for line in data.split('\n'):
        if not line:
            continue
            
        wid, tid, word, morph = line.split('\t')
        if morph == 'Type1':
            for r in res:
                tmp_sen = r + [empty[:], empty[:], empty[:]]
                result.append(tmp_sen[:7])
            res = []
            sentence = []
        else:
            to_remove = []
            # add to every 7gram next value
            for i in range(len(res)):
                if len(res[i]) == 7:
                    # adding to result set
                    result.append(res[i][:])
                    to_remove.append(i)
                else:
                    res[i].append(chain2bin(morph) if wid not in disamed else chain2bin(disamed[wid]))
                    
            # if word is disamed, then add beginning of it 7gram
            if wid in disamed:
                tmp_sen = [empty[:], empty[:], empty[:]] + sentence
                res.append(tmp_sen[-3:] + [(morph, chain2bin(disamed[wid]))])
                
            # remove 7grams that was directed to result
            for i in to_remove[::-1]:
                res.remove(res[i])

    return result

def load_ngrams(filename):
    with open(filename, 'rb') as stream:
        data = stream.read().decode('utf-8')
    
    result = []
    for line in data.split('\n'):
        if not line:
            continue
        words = line.split('\t')
        result.append(([chain2bin(word) for word in words]))
    
    return result




