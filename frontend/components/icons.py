from idom import vdom

batch_action = vdom(
    "svg",
    {
        "class": "mr-4 fill-filter-name",
        'width': "14",
        'height': "11"
    },
    vdom(
        "path",
        {
            "d": "M9.01719 5.3092C9.25519 5.0777 9.63469 5.0832 9.86569 5.3222C10.0962 5.5602 10.0907 5.9397 9.85269 6.1702L5.71009 10.1173C5.59359 10.2303 5.44259 10.2868 5.29209 10.2868C5.14159 10.2868 4.99059 10.2303 4.87459 10.1173L0.731084 6.1702C0.493584 5.9397 0.487584 5.5602 0.718084 5.3222C0.949084 5.0832 1.32908 5.0777 1.56658 5.3092L4.69209 8.2693V1.71338C4.69209 1.16109 5.1398 0.713379 5.69209 0.713379H12.7876C13.154 0.713379 13.451 1.01041 13.451 1.37681C13.451 1.74321 13.154 2.04024 12.7876 2.04024H6.39209C6.11594 2.04024 5.89209 2.2641 5.89209 2.54024V3.30075V8.2693L9.01719 5.3092Z",
        },
    ),
)

filter = vdom(
    "svg",
    {
        "class": "mr-4 fill-filter-name",
        'width': "15",
        'height': "17"
    },
    vdom(
        "path",
        {
            "fill-rule": "evenodd",
            "clip-rule": "evenodd",
            "d": "M8.34051 15.2965C8.34851 15.2995 8.36701 15.3045 8.39101 15.287C8.40701 15.275 8.42651 15.252 8.42651 15.211V10.5327C8.42651 9.05023 9.11099 7.63028 10.2595 6.72781L13.0949 4.05339C13.1764 3.97639 13.2284 3.87039 13.2409 3.7549L13.4444 1.89496C13.4524 1.82146 13.4194 1.77296 13.3994 1.74996C13.3789 1.72696 13.3434 1.69996 13.2914 1.69996H1.35373C1.30173 1.69996 1.26673 1.72696 1.24623 1.74996C1.22574 1.77246 1.19324 1.82096 1.20074 1.89446L1.40723 3.8339C1.41973 3.95139 1.47273 4.05889 1.55672 4.13689L4.35214 6.72531C5.5231 7.62728 6.22108 9.05723 6.22108 10.5577V14.5746C6.22108 14.6146 6.24408 14.6506 6.27558 14.6606L8.34051 15.2965ZM8.35951 16.5C8.23552 16.5 8.11052 16.4815 7.98752 16.4435H7.98702L5.92209 15.807C5.38311 15.641 5.02112 15.1455 5.02112 14.5746V10.5577C5.02112 9.42022 4.49063 8.33775 3.60216 7.66278L3.55766 7.62528L0.74125 5.01686C0.44426 4.74187 0.257265 4.36688 0.213767 3.96089L0.00777327 2.02145C-0.0337254 1.62996 0.0922706 1.23848 0.353762 0.947486C0.609754 0.662995 0.974243 0.5 1.35373 0.5H13.2914C13.6718 0.5 14.0368 0.663495 14.2928 0.948986C14.5543 1.24098 14.6798 1.63296 14.6368 2.02545L14.4338 3.88539C14.3903 4.28388 14.2073 4.65337 13.9183 4.92636L11.0179 7.65778C10.1465 8.33376 9.62647 9.40822 9.62647 10.5327V15.211C9.62647 15.621 9.43098 16.0105 9.10399 16.2525C8.883 16.4155 8.624 16.5 8.35951 16.5Z",
        },
    ),
)

edit = vdom(
    "svg",
    {
        "class": "mr-4 fill-filter-name",
        'width': "16",
        'height': "17"
    },
    vdom(
        "path",
        {
            "fill-rule": "evenodd",
            "clip-rule": "evenodd",
            "d": "M14.3958 13.8495V9.28808C14.3958 8.95658 14.1268 8.68808 13.7958 8.68808C13.4643 8.68808 13.1958 8.95658 13.1958 9.28808V13.8495C13.1958 14.453 12.7038 14.9435 12.0988 14.9435H2.29747C1.69248 14.9435 1.20048 14.453 1.20048 13.8495V4.06515C1.20048 3.46166 1.69248 2.97117 2.29747 2.97117H7.1979C7.52939 2.97117 7.79839 2.70217 7.79839 2.37067C7.79839 2.03968 7.52939 1.77068 7.1979 1.77068H2.29747C1.03099 1.77068 0 2.80017 0 4.06515V13.8495C0 15.1145 1.03099 16.1435 2.29747 16.1435H12.0988C13.3653 16.1435 14.3958 15.1145 14.3958 13.8495ZM5.43742 9.22308L5.27392 10.8911L6.9649 10.7871L12.5998 5.39413L11.0768 3.82565L5.43742 9.22308ZM4.60843 12.1335C4.44594 12.1335 4.28994 12.068 4.17644 11.95C4.05444 11.8235 3.99394 11.65 4.01094 11.475L4.26444 8.88458C4.27844 8.74208 4.34344 8.60909 4.44694 8.50959L10.6773 2.54717C10.9158 2.31918 11.2928 2.32618 11.5228 2.56267L13.8818 4.99164C13.9933 5.10664 14.0543 5.26063 14.0513 5.42063C14.0483 5.58063 13.9818 5.73263 13.8663 5.84313L7.63539 11.806C7.53339 11.9035 7.39939 11.9625 7.2579 11.971L4.64543 12.1325C4.63293 12.133 4.62043 12.1335 4.60843 12.1335ZM13.1543 1.81218L14.6773 3.38066L14.7623 3.29916C14.7928 3.26966 14.7998 3.23616 14.8003 3.21316C14.8008 3.19016 14.7948 3.15616 14.7653 3.12566L13.4178 1.73868C13.3683 1.68718 13.2853 1.68568 13.2338 1.73568L13.1543 1.81218ZM14.6628 4.82664C14.5063 4.82664 14.3498 4.76564 14.2323 4.64464L11.8733 2.21518C11.7618 2.10068 11.7008 1.94618 11.7038 1.78668C11.7063 1.62718 11.7728 1.47469 11.8878 1.36419L12.4028 0.870196C12.9288 0.364203 13.7708 0.378703 14.2793 0.902695L15.6263 2.28968C15.8733 2.54417 16.0063 2.87967 15.9998 3.23416C15.9938 3.58866 15.8493 3.91915 15.5933 4.16465L15.0783 4.65964C14.9618 4.77114 14.8123 4.82664 14.6628 4.82664Z",
        },
    ),
)

delete = vdom(
    "svg",
    {
        "class": "mr-4 fill-filter-name",
        'width': "14",
        'height': "17"
    },
    vdom(
        "path",
        {
            "fill-rule": "evenodd",
            "clip-rule": "evenodd",
            "d": "M8 11.59V6.481C8 6.149 8.269 5.881 8.6 5.881C8.932 5.881 9.2 6.149 9.2 6.481V11.59C9.2 11.922 8.932 12.19 8.6 12.19C8.269 12.19 8 11.922 8 11.59ZM4.601 11.59V6.481C4.601 6.149 4.869 5.881 5.201 5.881C5.532 5.881 5.801 6.149 5.801 6.481V11.59C5.801 11.922 5.532 12.19 5.201 12.19C4.869 12.19 4.601 11.922 4.601 11.59ZM10.909 14.168C10.884 14.803 10.368 15.3 9.734 15.3H4.067C3.433 15.3 2.917 14.803 2.892 14.168L2.483 3.652H11.318L10.909 14.168ZM5.8 1.7H8.001L8.093 2.452H5.708L5.8 1.7ZM13.2 2.452H9.302L9.169 1.367C9.108 0.873 8.687 0.5 8.189 0.5H5.612C5.114 0.5 4.692 0.873 4.631 1.368L4.499 2.452H0.601C0.269 2.452 0 2.72 0 3.052C0 3.383 0.269 3.652 0.601 3.652H1.282L1.693 14.215C1.743 15.496 2.786 16.5 4.067 16.5H9.734C11.015 16.5 12.058 15.496 12.108 14.215L12.519 3.652H13.2C13.532 3.652 13.8 3.383 13.8 3.052C13.8 2.72 13.532 2.452 13.2 2.452Z",
        },
    ),
)

done = vdom(
    "svg",
    {
        "class": "mr-4 fill-filter-name",
        'width': "16",
        'height': "17"
    },
    vdom(
        "path",
        {
            "fill-rule": "evenodd",
            "clip-rule": "evenodd",
            "d": "M7.742 11.0527L15.395 3.37736C15.6295 3.14268 15.6295 2.76157 15.395 2.52639C15.1605 2.29121 14.7805 2.29121 14.5465 2.52639L7.3175 9.77596L4.592 7.04251C4.3575 6.80733 3.9775 6.80733 3.7435 7.04251C3.509 7.2777 3.509 7.6583 3.7435 7.89349L6.8935 11.0527C7.0105 11.17 7.164 11.2292 7.3175 11.2292C7.4715 11.2292 7.625 11.17 7.742 11.0527ZM13.5895 16.5H2.411C1.0815 16.5 0 15.4153 0 14.082V2.91753C0 1.58465 1.0815 0.5 2.411 0.5H9.691C10.0225 0.5 10.291 0.769784 10.291 1.10175C10.291 1.43422 10.0225 1.7035 9.691 1.7035H2.411C1.7435 1.7035 1.2 2.24808 1.2 2.91753V14.082C1.2 14.7514 1.7435 15.296 2.411 15.296H13.5895C14.257 15.296 14.8 14.7514 14.8 14.082V7.94213C14.8 7.60966 15.069 7.34038 15.4 7.34038C15.7315 7.34038 16 7.60966 16 7.94213V14.082C16 15.4153 14.9185 16.5 13.5895 16.5Z",
        },
    ),
)

arrow_right = vdom(
    "svg",
    {
        "class": "fill-text",
        'width': "7",
        'height': "11"
    },
    vdom(
        "path",
        {
            "fill-rule": "evenodd",
            "clip-rule": "evenodd",
            "d": "M1.44203 10.7502C1.29099 10.7502 1.13897 10.6912 1.02347 10.5743C0.792472 10.3403 0.792472 9.96025 1.02248 9.72625L4.94649 5.75025L1.02248 1.77425C0.792472 1.54025 0.792472 1.16025 1.02347 0.92625C1.25546 0.69125 1.62959 0.69125 1.86158 0.92625L5.86259 4.98025C6.24067 5.42725 6.24067 6.07325 5.89319 6.48525L1.86158 10.5743C1.74608 10.6912 1.59307 10.7502 1.44203 10.7502Z",
        },
    ),
)

arrow_left = vdom(
    "svg",
    {
        "class": "fill-text",
        'width': "6",
        'height': "11"
    },
    vdom(
        "path",
        {
            "fill-rule": "evenodd",
            "clip-rule": "evenodd",
            "d": "M5.20812 0.749994C5.35915 0.749994 5.51118 0.808994 5.62668 0.925994C5.85767 1.15999 5.85767 1.53999 5.62766 1.77399L1.70366 5.74999L5.62766 9.72599C5.85767 9.95999 5.85767 10.34 5.62668 10.574C5.39469 10.809 5.02055 10.809 4.78857 10.574L0.78756 6.51999C0.409473 6.07299 0.409473 5.42699 0.756958 5.01499L4.78857 0.925994C4.90407 0.808994 5.05708 0.749994 5.20812 0.749994Z",
        },
    ),
)
