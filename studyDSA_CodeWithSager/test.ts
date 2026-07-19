enum ExpressionType {
    FUNCTION,
    NUMMERIC,
    TEXT
}

abstract class Expression {
    constructor(public type: ExpressionType) { }
}

class NummericExpression extends Expression {
    constructor(public value: number) {
        super(ExpressionType.NUMMERIC);
    }
}

class TextExpresion extends Expression {
    constructor(public value: string) {
        super(ExpressionType.TEXT);
    }
}

class FunctionExpression<ReturnType> extends Expression {
    declare readonly _phantomType: ReturnType;

    public readonly args: Array<Expression | undefined>;

    constructor(
        public readonly name: string,
        ...args: Array<Expression | undefined>
    ) {
        super(ExpressionType.FUNCTION);
        this.args = args;
    }

    toString(): string {
        const argList = this.args.join(", ");
        return `${this.name}(${argList})`;
    }
}

type SumArgs = NummericExpression | FunctionExpression<NummericExpression>;
const SUM = (...args: Array<SumArgs>): FunctionExpression<NummericExpression> => {
    return new FunctionExpression<NummericExpression>("SUM", ...args);
};

type ConcatArgs = TextExpresion | FunctionExpression<TextExpresion>;
const CONCAT = (...args: Array<ConcatArgs>): FunctionExpression<TextExpresion> => {
    return new FunctionExpression<TextExpresion>("CONCAT", ...args);
};

const num1 = new NummericExpression(10);
const num2 = new NummericExpression(20);
const text1 = new TextExpresion("hello");

const validSum = SUM(num1, num2);
const validConcat = CONCAT(text1, new TextExpresion("world"));

const brokenFormula = SUM(CONCAT(text1, text1));