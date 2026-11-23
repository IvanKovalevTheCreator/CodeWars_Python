def remove_url_anchor(url):
    # TODO: complete
    clear_url = ""
    for i in url:
        if i != "#":
            clear_url += i
        else:
            break
    return clear_url
