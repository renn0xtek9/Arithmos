
[ "$RUN_PYLINT" ] && return 0   # Nothing to do

for script in \
    install_arithmos.sh    \
    install_postgres.sh  \
    install_mssql.sh    \
    install_pyqt.sh
do
    foldable source $TRAVIS_BUILD_DIR/.travis/$script
done
