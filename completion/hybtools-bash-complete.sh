_hybtools_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _HYBTOOLS_COMPLETE=complete $1 ) )
    return 0
}

complete -F _hybtools_completion -o default hybtools;
