import "./newpost.css"

const NewPost = () => {

    const uploadPost = () => {

        fetch("http://127.0.0.1:5000/posts")

    }

    return (
        <div className="NewPost">
            <textarea placeholder="what's on your mind?"></textarea>
            <div className="newpost-buttons">
                <input id="newPostImage" name="image" type="file" accept=".png,.jpg,.jpeg"></input>
                <label htmlFor="image">upload</label>
                <button onClick={uploadPost}>Post</button>
            </div>
        </div>
    )
}

export default NewPost