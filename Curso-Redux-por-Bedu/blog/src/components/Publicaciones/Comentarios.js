import { connect } from 'react-redux';
import Spinner from '../General/Spinner';
import Fatal from '../General/Fatal';

const Comentarios = (props) => {
  console.log('ca')
  if (props.com_cargando) {
    return <Spinner />
  }
  if (props.com_error) {
    return <Fatal mensaje={props.com_error} />
  }

  const ponerComentarios = () => (
    
    props.comentarios.map((comentario) => (
      
      <li key={comentario.id}>
        <b><u>{comentario.email}</u></b>
        <br />
        { comentario.body}
      </li>
    ))
  );

  return (
    <ul>
      { ponerComentarios()}
    </ul>
  );
};

const mapStateToProps = ({ publicacionesReducer }) => publicacionesReducer;

export default connect(mapStateToProps)(Comentarios);