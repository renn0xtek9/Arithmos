cd "$TRAVIS_BUILD_DIR"

# Decrypt private key
openssl aes-256-cbc -K $encrypted_3fc26dee5a84_key -iv $encrypted_3fc26dee5a84_iv -in .travis/upload_doc_id -out .travis/key.private -d
chmod 700 .travis/key.private

# Upload the docs
mkdir doc/arithmos3doc
cp -r doc/data-mining-library/build/html doc/arithmos3doc/data-mining-library
cp -r doc/development/build/html doc/arithmos3doc/development
cp -r doc/visual-programming/build/html doc/arithmos3doc/visual-programming
> ~/.ssh/config echo "
Host biolab.si
    StrictHostKeyChecking no
    User uploaddocs
    IdentityFile $TRAVIS_BUILD_DIR/.travis/key.private
"
rsync -a --delete doc/arithmos3doc/ biolab.si:/arithmos3doc/
