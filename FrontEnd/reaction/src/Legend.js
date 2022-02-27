import FormEntry from "./FormEntry"

function Legend(props) {

    const lst = props.options;
    const checkboxes = lst.map((e, i) => {
        return <FormEntry test={e} key={i} />
    })

    return <div>
        <form>
            <fieldset>
                <legend>{props.title}</legend>
                {checkboxes}
            </fieldset>
        </form>
    </div>;

}

export default Legend