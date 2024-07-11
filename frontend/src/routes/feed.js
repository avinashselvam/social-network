import { useEffect } from "react"
import NewPost from "../components/newpost"
import Post from "../components/post"
import PeopleYouMayKnow from "../components/peopleyoumayknow"

import "./feed.css"

const Feed = () => {

    return (
        <div className="Feed">
            <div className="posts">
                <NewPost />
                <Post />
            </div>
            <PeopleYouMayKnow />
        </div>
    )

}

export default Feed