#!/bin/bash

# For move and resize windown more convenient via Keyboard shortcuts

usage()
{
    echo -e "\tFor move and resize the current active window"
    echo -en "\twmctrl & xdpyinfo are needed, Ensure them were installed\n"
    echo -e "\t-h display this help"
    echo -e "\t-m margin: distance to the screen boundary. Default=10"
    echo -en "\t-p format of -m values. Default is percent, -p means pixel\n"
    exit 1
}

error()
{
    echo "$1"
    exit 2
}

# check related tools
wmctrl > /dev/null 2>&1
[ $? == 127 ] && usage
xdpyinfo > /dev/null 2>&1
[ $? == 127 ] && usage

set -u
set -e

min_length=400

start()
{
    # FIXME detect the REAL AVAILABLE dimensions should use `wmctrl -d`
    # And `xdpyinfo` is no longer needed
    dimensions=`xdpyinfo | grep dimensions | awk '{print $2}'`
    width=`echo $dimensions | awk -F x '{print $1}'`
    height=`echo $dimensions | awk -F x '{print $2}'`

    if [[ $unit -eq 0 ]]
    then
        width_margins=$((width*margin/100))
        height_margins=$((height*margin/100))
    else
        width_margins=$margin
        height_margins=$margin
    fi

    new_width=$((width - width_margins*2))
    new_height=$((height - height_margins*2))

    [[ $new_width -lt $min_length || $new_height -lt $min_length ]] && error "new width, height too narrow"

    # move & resize
    wmctrl -r :ACTIVE: -e 0,$width_margins,$height_margins,$new_width,$new_height
}


margin=10
unit=0  # 0 - percent, 1 - pixel

while getopts d:m:ph arg
do
    case "$arg" in
        d)
            # TODO delay n secs.
            ;;
        m)
            margin=$OPTARG
            ;;
        p)
            unit=1
            ;;
        h)
            usage
            ;;
        ?)
            usage
            ;;
    esac
done

[[ $margin -lt 0 ]] && error "margin must be a positive number" 

start

exit 0
