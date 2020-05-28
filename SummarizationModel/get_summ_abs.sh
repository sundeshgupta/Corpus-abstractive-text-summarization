#!/bin/bash

export CLASSPATH=./stanford-corenlp-4.0.0/stanford-corenlp-4.0.0.jar

cat ./IO/in.txt > ./stories/test.story

printf "\n\n@highlight\n\nNothing here\n\n" >> ./stories/test.story

python3 make_datafiles.py ./stories ./output

python3 run_summarization.py --mode=decode --data_path=./output/finished_files/test* --vocab_path=./vocab --log_root=./ --exp_name=pretrained_model --max_enc_steps=400 --max_dec_steps=120 --coverage=1 --single_pass=1

cat ./pretrained_model/decode_test_400maxenc_4beam_35mindec_120maxdec_ckpt-238410/decoded/000000_decoded.txt > ./IO/out.txt

rm -r ./pretrained_model/decode_test_400maxenc_4beam_35mindec_120maxdec_ckpt-238410

rm ./output/tokenized_stories_dir/test.story


