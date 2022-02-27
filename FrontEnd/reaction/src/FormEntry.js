function FormEntry(props) {
    return (
        <div>
            <input type="checkbox" id={props.test} name="interest" value={props.test} c/>
            <label for={props.test}>{props.test}</label>
        </div>
    );
}

export default FormEntry;