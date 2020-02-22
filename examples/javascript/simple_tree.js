/*
Simple tree class in Javascript.

Command to run:

    node simple_tree.js


Copyright © 2020 Stephen McEntee
Licensed under the GNU Affero General Public License v3.0. 
See LICENSE file for details:
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/javascript/LICENSE

Includes code sourced from https://github.com/aureooms/js-itertools
Licence https://github.com/aureooms/js-itertools/blob/master/LICENSE
*/



// https://github.com/aureooms/js-itertools/
let iterchain = function* ( iterables ) {
    for ( let iterable of iterables ) yield* iterable
}


class Node {
    constructor(name, parent=null, data={vn_type: "default"}) {
        this.name = name
        this.parent = parent
        this.childs = []
        if (parent !== null) {
            parent.add_child(this)
        }
        if (data) this.merge_nodeObj(data)
        // this.walkTree = this.map   // renaming method
    // console.log("class Node this", this)
    // console.log("class Node data", data)
    // for (let key in data) {
    //     if (data.hasOwnProperty(key)) console.log("key=",key, "data[key]=", data[key])
    // }
    // console.log("class Node data.childs", data["childs"])
    // console.log("class Node this.name", this.name)
    // console.log("class Node this.vn_type", this.vn_type)
    //  console.log("class Node this.childs", this.childs)
    }

    merge_nodeObj(nodeObj) {
        for (let key in nodeObj) {
            if (["parent", "childs"].includes(key)) continue
            this[key] = nodeObj[key]
        }
        //if ("childs" in nodeObj) {    // not safe
        if (nodeObj.hasOwnProperty("childs")) {
            for (let childObj of nodeObj.childs) {
                new Node(null, this, childObj) // parent.add_child in constructor
            }
        }
    }

    add_child (newchild) {
        this.childs.push(newchild)
        newchild.parent = this
    }
    
    // DELETE this method, do not use
    in_data(attr) {
        if( this.data.hasOwnProperty( attr ) ) return true; 
        return false;
    }

    get_node(coord=null) {
        let _curnode
        if (coord) {
            //if(!this.hasOwnProperty("tr_coord")) return null // see toAnlzTreeObj
            _curnode = get_node() // get root node
            for (let ii =0; ii < coord.length; ii++) {
                _curnode = _curnode.childs[coord[ii]]
            }
            return _curnode
        } else {   // get root node
            _curnode = this
            while (_curnode.parent) {
                _curnode = _curnode.parent
            }
            return _curnode
        }
    }

    get_ancestors() {
        let _curnode=this, ancestors=[]
        while (_curnode.parent) {
            _curnode = _curnode.parent
            ancestors.push(_curnode)
        }
        return ancestors
    }

    *traverse() {
        yield this;
        for (let child of iterchain(this.childs)) {
            yield child;
        }
    }
    
    [Symbol.iterator]() {
        return this.traverse();
    }

    walkTree(func, ...Args) {     // rename to map??
        // NOTE: use ordinary function for func (not an arrow function, because of lexical binding this)
        // http://reactkungfu.com/2015/07/why-and-how-to-bind-methods-in-your-react-component-classes/
        for (let node of this) {
            func.bind(node)(...Args)
        } 
    }

    async walkTreeAsync(func, ...Args) {
        for (let node of this) {
            await func.bind(node)(...Args)
        } 
    }

    toTextTree(tabLevel=-1) {
        let nodetext = "";
        tabLevel += 1;
        for (let i =0; i < tabLevel; i++) {
            nodetext += ".   ";
        }
        nodetext += "|---" + this.name + "\n";   
        for (let child of this.childs) {
            nodetext += child.toTextTree(tabLevel);
        }
        return nodetext;
    }

    toTreeObj(full=true) {
        let treeObj = {}
        if (full) { 
            let nodeAttrs = Object.keys(this)
            delete nodeAttrs.childs;
            delete nodeAttrs.parent;
            for (let key of nodeAttrs) treeObj[key] = this[key]
        } else {
            for (let key of ["_id", "name", "fs_path"]) treeObj[key] = this[key]
        }
        if (this.childs.length) {
            treeObj.childs = []
            for (let child of this.childs) {
                treeObj.childs.push(child.toTreeObj(full))
            }
        }
        return treeObj
    }

    toAnlzTreeObj(trCoord=[]) {
        let treeObj = {}, attrsList, childCount, _nodeObj  
        treeObj.tr_coord = trCoord
        treeObj.tr_type = "LEAF"
        attrsList = ["_id", "name", "fs_path"]
        for (let key of attrsList) {
            if(this.hasOwnProperty(key)) treeObj[key] = this[key]
        }
        if (this.childs.length) {
            treeObj.tr_type = "GROUP"
            treeObj.childs = []
            treeObj.tr_childCount = 0
            treeObj.tr_childGroupCount = 0
            for (let child of this.childs) {
                _nodeObj = child.toAnlzTreeObj(_.concat(trCoord, treeObj.tr_childCount))
                treeObj.childs.push(_nodeObj)
                treeObj.tr_childCount++
                if (_nodeObj.tr_type === "GROUP") treeObj.tr_childGroupCount++
            }
        }
        return treeObj
    }

    // introspect tree
    toAnlzTree() {
        let _anlzObj = this.toAnlzTreeObj()
        return new Node(null, null, _anlzObj)
    }


    toJsTree() {
        let type = "default";
        if ("vn_jstreetype" in this)  type = this.vn_jstreetype
        let data = {}
        //for (let key of ["fs_filepath", "_id", "_dbid"]) {
        for (let key of ["name", "fs_path", "_id"]) {
            if (key in this) data[key] = this[key]
        }
        let jstree = { text: this.name,
                       data,
                       type };
        if (this.childs.length) {
            jstree.children = [];
            for (let child of this.childs) {
                jstree.children.push(child.toJsTree());
            }
        }
        return jstree;
    }

    toDBObj() {
        let dbObj = {}
        let nodeAttrs = Object.keys(this)
        _.pull(nodeAttrs, "childs", "parent")
        for (let key of nodeAttrs) {
            dbObj[key] = this[key]
        }        
        if (this.parent) {
            dbObj.parent = this.parent._id
        } else {
            dbObj.parent = null
        }
        if (this.childs.length) {
            dbObj.childs = []
            for (let child of this.childs) {
                dbObj.childs.push(child._id)
            }
        }
        return dbObj        
    }

}


// TESTS: just set to true|false, require.main===module does not work with Babel
let run_tests = false
if (run_tests || require.main===module) {
    console.log("Launching tests for ", __filename)
    runTests()
}

function runTests() {
    let rootnode = new Node("root node");
    let node1 = new Node("node1 level1", rootnode);
    let node11 = new Node("node11 level2", node1);
    let node12 = new Node("node12 level2", node1);
    let node13 = new Node("node13 level2", node1);
    let node121 = new Node("node121 level3", node12);
    let node122 = new Node("node122 level3", node12);
    let node2 = new Node("node2 (level1)", rootnode);
    let node21 = new Node("node21 (level2)", node2);
    let node211 = new Node("node211 (level3)", node21);
    let node212 = new Node("node212 (level3) parentless");
    node21.add_child(node212);
    node21.add_child(new Node("node213 (level3) parentless"));
    let node3 = new Node("node3 (level1)", rootnode);
    for (let node of rootnode)  console.log(node.name) // iterate over tree
    console.log(rootnode.toTextTree());
    //console.log(JSON.stringify(rootnode.toJsTree(), null, 2));
    //console.log(node2.toTextTree());
    //console.log(JSON.stringify(rootnode.toTreeObj(), null, 2)) 
    let newnode = new Node("", null, rootnode.toTreeObj()) // create new tree using Obj from first tree
    console.log(newnode.toTextTree())
}

module.exports = Node;
