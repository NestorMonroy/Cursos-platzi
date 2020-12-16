import React from "react";
import { Link } from "react-router-dom";
import Badge from "../components/Badge";
import Modal from "../components/Modal";
import DeleteBadgeModal from "../components/DeleteBadgeModal";
import confLogo from "../images/platziconf-logo.svg";
import "./styles/BadgeDetails.css";

function useIncreaseCount(max){
  const [count, setCount] = React.useState(0)
  if(count > max){
    setCount(0)
  }

  return[count, setCount]

}

function BadgeDetails(props) {
  const [count, setCount] = useIncreaseCount(4)

  
  const badge = props.badge;
  return (
    <div>
      <div className="BadgeDetails__hero">
        <div className="container">
          <div className="row">
            <div className="col-6">
              <img src={confLogo} alt="Logo de la conferencia" />
            </div>
            <div className="col-6 BadgeDetails__hero-attendant-name">
              <h1>
                {" "}
                {badge.firstName} {badge.lastName}{" "}
              </h1>
            </div>
          </div>
        </div>
      </div>
      <div className="container">
        <div className="row">
          <div className="col">
            <Badge
              firstName={badge.firstName}
              lastName={badge.lastName}
              email={badge.email}
              twitter={badge.twitter}
              jobTitle={badge.jobTitle}
            />
          </div>
          <div className="col">
            <h2>Actions</h2>
            <div>
              <div>
                <Link
                  className="btn btn-primary mb-4"
                  to={`/badges/${badge.id}/edit`}
                >
                  Edit
                </Link>
                <button onClick={() => {
                  setCount(count+1)
                }} className="btn btn-primary ml-4">
                  Increase Count: {count}
                </button>
              </div>
              <div>
                <button onClick={props.onOpenModal} className="btn btn-danger">
                  Delete
                </button>
                <DeleteBadgeModal
                  isOpen={props.modalIsOpen}
                  onClose={props.onCloseModal}
                  onDeleteBagde={props.onDeleteBagde}
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default BadgeDetails;
