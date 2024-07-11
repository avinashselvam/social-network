import "./post.css"

const Post = () => {

    return (
        <div className="Post">
            <div className="post-userdetails">
                <div className="left">
                    <img className="post-pp" src="data:"></img>
                </div>
                <div className="right">
                    <p className="post-username">Avinash</p>
                    <p className="post-time">just now</p>
                </div>
            </div>
            <div className="post-content">
                <p className="post-text">post text</p>
                <img className="post-img"></img>
            </div>
        </div>
    )

}

export default Post